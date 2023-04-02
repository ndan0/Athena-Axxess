from transformers import pipeline

def model_load():
    
    classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)
    
    return classifier
