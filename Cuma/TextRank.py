from collections import OrderedDict
import numpy as np
import spacy
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.util import ngrams
from SentimentAnalysis import model_load


nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')

en_stop_words = set(stopwords.words('english'))
exclude = set(string.punctuation)
exclude.remove('-')
exclude.remove('&')
lemma = WordNetLemmatizer()
stemmer= PorterStemmer()
manual_removal_list = ['\'s','lot','bit','use','person','guy','look','way','people','company','kind', 'http', 'www', 'cookie', 'policy', 'privacy','interview','year','month','party']

medical_stopwords = ['patient',
'symptoms',
'symptom',
'medication',
'medications',
'dose',
'doctor',
'doctors',
'diagnosis',
'condition',
'conditions',
'treatment',
'treatments',
'test',
'tests',
'result',
'results',
'health',
'history',
'prescription',
'prescriptions',
'drug',
'drugs',
#'pain',
#'nausea',
#'headache',
#'fever',
#'cough',
#'sore throat',
#'diarrhea',
#'vomiting',
#'rash',
#'allergy',
#'allergies',
'side effects',
'effect',
'effects',
'medical',
'advice',
'referral',
'referrals',
'specialist',
'specialists',
'insurance',
'coverage',
'copay',
'deductible',
'pharmacy',
'pharmacies',]

nlp = spacy.load('en_core_web_sm', exclude=['ner'])

def scale_func(x):
    total = sum(x)
    return [k/total for k in x]

def custom_capital(text):
    if text.isupper():
        return text
    else:
        return text.lower()

class TextRank4Keyword():
    """Extract keywords from text"""
    
    def __init__(self):
        self.d = 0.85 # damping coefficient, usually is .85
        self.min_diff = 1e-7 # convergence threshold
        self.steps = 15 # iteration steps
        self.node_weight = None # save keywords and its weight
        self.error = False
        self.manual_removal_list = manual_removal_list
        self.pos_dict = {}

    def clean(self, sentences): #input format is text string, use after $from nltk.corpus import stopwords
        clean_sens = []
        for sen in sentences:
            numremoval = [i.strip('\’') for i in sen if not i.isdigit()]
            stopwordremoval = [i.lower() for i in numremoval if i not in en_stop_words]
            punctuationremoval = [ch for ch in stopwordremoval if ch not in exclude]
            normalized = [lemma.lemmatize(word) for word in punctuationremoval]
            normalized = [word for word in normalized if not word in manual_removal_list]
            clean_sens.append(normalized)
        return clean_sens
    
    def clean_doc_level(self, text):
        doc_segment = text.split('  ')
        pass_seg = []
        for seg in doc_segment:
            if not seg.startswith('function ') or len(seg)<2 or 'function(' in seg:
                pass_seg.append(seg)
        final_doc = ' '.join(pass_seg)
        return final_doc
    
    def ngram_prep(self, sentences):
        ngrams_list = []
        for sen in sentences:
            stopwordremoval = [custom_capital(i) for i in sen if i not in en_stop_words]
            manual_removal = [i.split('\'')[0] for i in stopwordremoval if i not in manual_removal_list]
            punctuationremoval = [ch for ch in manual_removal if ch not in exclude]
            normalized = [lemma.lemmatize(word) for word in punctuationremoval if len(word)>1]
            cleaned = [word for word in normalized if len(word)>1]
            candidate_ngram = ngrams(cleaned,2)
            
            #Reduce 'adj adj' kp case, only allow 'noun noun', 'adj noun' #ISSUE not solve 'adj adj' case yet
            ngram_list = []
            for (w1,w2) in candidate_ngram:
                tag_gram = nltk.pos_tag([w1, w2], tagset='universal')
                if tag_gram[1][1] == 'NOUN' or tag_gram[1][1] == 'PROPN':
                    ngram_list.append(w1+' '+w2)
            ngrams_list += ngram_list
        return ngrams_list
    
    def sentence_segment(self, doc, candidate_pos, lower=True):
        """Store those words only in cadidate_pos"""
        sentences = []
        for sent in doc.sents:
            selected_words = []
            selected_words_pos = []
            
            """NLTK version POS tag filtered"""
            #tag_sen = nltk.pos_tag(sent.text.split(), tagset='universal')
            #for word_tag in tag_sen:
            #    if word_tag[1] in candidate_pos and word_tag[0] not in manual_revomal_list:
            #        selected_words.append(word_tag[0])
            #sentences.append(selected_words)
            
            """Spacy version POS tag filtered"""
            for token in sent:
                #Store words only with cadidate POS tag
                if 'ADJ' not in candidate_pos:
                    if token.pos_ in candidate_pos:
                        selected_words.append(token.text)
                else:
                    if token.pos_ != 'ADJ' and token.pos_ in candidate_pos:
                        selected_words.append(token.text)
                        selected_words_pos.append(token.pos_)
                    elif token.pos_ == 'ADJ':
                        if selected_words_pos==[]:
                            selected_words.append(token.text)
                            selected_words_pos.append(token.pos_)
                        elif selected_words_pos[-1] == 'ADJ':
                            selected_words = selected_words[:-1]
                            selected_words.append(token.text)
                        elif selected_words_pos[-1] != 'ADJ':
                            selected_words.append(token.text)
                            selected_words_pos.append(token.pos_)

            sentences.append(selected_words)
        return sentences
        
    def get_vocab(self, sentences):
        """Get all tokens"""
        vocab = OrderedDict()
        i = 0
        for sentence in sentences:
            for word in sentence:
                if word not in vocab:
                    vocab[word] = i
                    i += 1
        return vocab
    
    def get_token_pairs(self, window_size, sentences):
        """Build token_pairs from windows in sentences"""
        token_pairs = list()
        for sentence in sentences:
            for i, word in enumerate(sentence):
                for j in range(i+1, i+window_size):
                    if j >= len(sentence):
                        break
                    pair = (word, sentence[j])
                    if pair not in token_pairs:
                        token_pairs.append(pair)
        return token_pairs
        
    def symmetrize(self, a):
        return a + a.T - np.diag(a.diagonal())
    
    def get_matrix(self, vocab, token_pairs):
        """Get normalized matrix"""
        # Build matrix
        vocab_size = len(vocab)
        g = np.zeros((vocab_size, vocab_size), dtype='float')
        for word1, word2 in token_pairs:
            #i, j = vocab[word1], vocab[word2] #original 
            j, i = vocab[word1], vocab[word2]
            g[i][j] = 1
            
        # Get Symmeric matrix
        g = self.symmetrize(g)
        
        # Normalize matrix by column
        norm = np.sum(g, axis=0)
        g_norm = np.divide(g, norm, where=norm!=0) # this is ignore the 0 element in norm
        
        return g_norm

    
    def get_keywords(self, number=10):
        """Print top number keywords"""
        if not self.error:
            node_weight = OrderedDict(sorted(self.node_weight.items(), key=lambda t: t[1], reverse=True))
            keyword_ordered_clean = [k for k in list(node_weight.keys())[:number] if len(k)<20 and len(k)>1]
            
            return [k for k in keyword_ordered_clean[:number]]
    
    def count_keyphrases(self, number=None):
        """Print top number keyphrases"""
        if not self.error:
            ngram_score = dict()
            for gram in self.ngrams:
                if gram not in ngram_score:
                    ngram_score[gram] = 1
                else:
                    ngram_score[gram] += 1
            ngram_score = OrderedDict(sorted(ngram_score.items(), key= lambda t: t[1], reverse=True))
            if number:
                return [k for k in list(ngram_score)[:number]]
            else:
                return [k for k in list(ngram_score.keys()) if ngram_score[k]>2]
        
    def analyze(self, text, 
                candidate_pos=['NOUN', 'PROPN'], 
                window_size=4, lower=False, stopwords=list(), cleaned=False):
        """Main function to analyze text"""
        if text != text:
            self.error = True
            print('TEXT IS NOT FOUND!')
        else:
            
            # Prepare spacy doc, and clean in general
            text = self.clean_doc_level(text)
            lower_doc = nlp(text.lower())
            doc = nlp(text)
            #self.doc = doc

            # Filter sentences
            sentences = self.sentence_segment(doc, candidate_pos) # list of list of words
            kp_sentences = self.sentence_segment(lower_doc, candidate_pos = ['NOUN', 'PRORN', 'ADJ'])

            #Preprocess the text
            if cleaned == False:
                clean_sentences = self.clean(sentences)
                clean_kp_sentences = self.clean(kp_sentences)
            
            self.kp_sentences = clean_kp_sentences
            self.ngrams = self.ngram_prep(clean_kp_sentences)

            # Build vocabulary
            vocab = self.get_vocab(clean_sentences)
            self.vocab = vocab

            # Get token_pairs from windows
            token_pairs = self.get_token_pairs(window_size, clean_sentences)

            # Get normalized matrix
            g = self.get_matrix(vocab, token_pairs)

            # Initionlization for weight(pagerank value)
            pr = np.array([1] * len(vocab))

            # Iteration for kw text rank
            previous_pr = 0
            for epoch in range(self.steps):
                pr = (1-self.d) + self.d * np.dot(g, pr)
                if abs(previous_pr - sum(pr))  < self.min_diff:
                    break
                else:
                    previous_pr = sum(pr)

            # Get weight for each node
            node_weight = dict()
            for word, index in vocab.items():
                node_weight[word] = pr[index]
            self.node_weight = node_weight

    def textrank_kp(self, window_size = 4):
        #Prepare kp (head, tail) pair to detect and transform the original doc/sens
        kp_connection_dict = {}
        kp_top_list = self.count_keyphrases(number=20)
        for kp in kp_top_list:
            head, tail = kp.split()
            if not head==tail and head in kp_connection_dict:
                kp_connection_dict[head].append(tail)
            elif not head==tail and head not in kp_connection_dict:
                kp_connection_dict[head] = [tail]
        
        processed_sens = []
        for sen in self.kp_sentences:
            processed_sen = []
            i=0
            while i < len(sen):
                current_word = sen[i]
                if i == len(sen)-1:
                    processed_sen.append(current_word)
                    i+=1
                elif current_word in kp_connection_dict and sen[i+1] in kp_connection_dict[current_word]:
                    processed_sen.append('_'.join([current_word, sen[i+1]]))
                    i+=2
                else:
                    processed_sen.append(current_word)
                    i+=1
            processed_sens.append(processed_sen)

        # Record processed sentences for kp
        self.processed_sens = processed_sens

        # Build vocabulary
        vocab = self.get_vocab(processed_sens)
        self.vocab = vocab

        # Get token_pairs from windows
        token_pairs = self.get_token_pairs(window_size, processed_sens)

        # Get normalized matrix
        g = self.get_matrix(vocab, token_pairs)

        # Initionlization for weight(pagerank value)
        pr = np.array([1] * len(vocab))

        # Iteration for kw text rank
        previous_pr = 0
        for epoch in range(self.steps):
            pr = (1-self.d) + self.d * np.dot(g, pr)
            if abs(previous_pr - sum(pr))  < self.min_diff:
                break
            else:
                previous_pr = sum(pr)

        # Get weight for each node
        kp_node_weight = dict()
        for word, index in vocab.items():
            if '_' in word:
                kp_node_weight[word] = pr[index]
        self.kp_node_weight = kp_node_weight  

        return list(kp_node_weight.keys())[:15]
    
if __name__ == '__main__':
    
    # Load in the extractor
    trk = TextRank4Keyword()
    
    # Load in the user input
    print("Input your corpus:\n")
    txt = input()
    
    # Analysis
    trk.analyze(txt)
    kw = trk.get_keywords()
    kw = '|'.join(kw)
    print(kw)
    
    # Sentiment model load in
    model = model_load()
    sentiment = model(txt)
    print(sentiment[0])