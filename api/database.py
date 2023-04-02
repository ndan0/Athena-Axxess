import firebase_admin
from firebase_admin import credentials, firestore
import datetime
import random

start_date = datetime.datetime(2023, 1, 1)
dates = [start_date + datetime.timedelta(days=i) for i in range(51)]


db = firestore.client()  # this connects to our Firestore database
collection = db.collection('query-db')  # opens 'query-db' collection

queries = [
    "I've been feeling very tired lately.",
    "I've been experiencing some shortness of breath when exercising.",
    "I've had a headache that won't go away for a few days now.",
    "I've been having difficulty sleeping and staying asleep.",
    "I've been experiencing a persistent cough and chest pain.",
    "I've been feeling very anxious and stressed lately.",
    "I've been having trouble with my vision and seeing double sometimes.",
    "I've been experiencing a lot of joint pain in my knees and hips.",
    "I've been having trouble concentrating and focusing on my work.",
    "I've been feeling dizzy and lightheaded frequently.",
    "I've been experiencing abdominal pain and discomfort.",
    "I've noticed a lump or growth on my body that concerns me.",
    "I've been experiencing numbness and tingling in my hands and feet.",
    "I've been feeling very depressed and hopeless lately.",
    "I've been having trouble with my memory and forget things easily.",
    "I've been experiencing skin rash or irritation on my arms and legs.",
    "I've been having trouble with my balance and falling down frequently.",
    "I've been experiencing frequent headaches and migraines.",
    "I've been feeling very irritable and easily angered lately.",
    "I've been experiencing a lot of back pain and stiffness.",
    "I've been having trouble with my hearing and hearing muffled sounds.",
    "I've been feeling very lonely and isolated lately.",
    "I've been experiencing chest pain and heart palpitations.",
    "I've been having trouble with my digestion and experiencing bloating and constipation.",
    "I've been experiencing shortness of breath and wheezing.",
    "I've been feeling very hopeless and helpless lately.",
    "I've been experiencing muscle weakness and fatigue.",
    "I've been having trouble with my balance and coordination.",
    "I've been experiencing tremors and shaking in my hands.",
    "I've been feeling very agitated and restless lately.",
    "I've been experiencing chest pain and shortness of breath during exercise.",
    "I've been having trouble with my balance and experiencing dizziness.",
    "I've been experiencing nausea and vomiting frequently.",
    "I've been feeling very worried and anxious about the future.",
    "I've been having trouble with my memory and forget things easily.",
    "I've been experiencing difficulty swallowing and choking on food.",
    "I've been experiencing shortness of breath and tightness in my chest.",
    "I've been feeling very overwhelmed and stressed lately.",
    "I've been having trouble with my balance and falling down frequently.",
    "I've been experiencing frequent urination and thirst.",
    "I've been feeling very angry and irritable lately.",
    "I've been experiencing pain and stiffness in my neck and shoulders.",
    "I've been having trouble with my balance and experiencing vertigo.",
    "I've been experiencing frequent nosebleeds and sinus congestion.",
    "I've been feeling very sad and hopeless lately.",
    "I've been experiencing chest pain and pressure.",
    "I've been having trouble with my digestion and experiencing stomach cramps.",
    "I've been experiencing shortness of breath and difficulty breathing.",
    "I've been feeling very stressed and overwhelmed by work.",
    "I've been experiencing muscle cramps and spasms.",
    "I've been having trouble with my coordination and balance."]

id = 0
for i in range(0, len(dates)):
    print(i)
    res = collection.document(str(id)).set({
        "Date": datetime.datetime.strftime(dates[i], '%Y-%m-%d'),
        "Keywords": "",
        "Query": queries[i],
        "Sentiment": [0,0,0,0],
        "Risk": 0
    })
    id = id + 1