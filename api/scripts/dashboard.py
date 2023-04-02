import firebase_admin
from datetime import datetime
from firebase_admin import credentials, firestore

# cred = credentials.Certificate("./secret.json")
# firebase_admin.initialize_app(cred)

db = firestore.client()  # this connects to our Firestore database
collection = db.collection('query-db')  # opens 'query-db' collection

def get_emotion(start_date, num_of_days):
    dt = datetime.strptime(start_date, '%Y-%m-%d')
    # Define number of days to add to start date
    n_days = num_of_days

    # Calculate end date
    end_date = start_date + datetime.timedelta(days=n_days)

    # Query documents with date field between start_date and end_date
    docs = collection.where('date', '>=', start_date).where('date', '<=', end_date).get()

    result = []
    # Iterate through the documents and extract the desired field
    for doc in docs:
        obj = {
            "date" : doc.to_dict()["Date"].strptime(start_date, '%Y-%m-%d'),
            "emotions" : doc.to_dict()["Sentiment"]
            
        }
        result.append(obj)

    print(result)   

def get_keywords(start_date, num_of_days):
    dt = datetime.strptime(start_date, '%Y-%m-%d')
    # Define number of days to add to start date
    n_days = num_of_days

    # Calculate end date
    end_date = start_date + datetime.timedelta(days=n_days)

    # Query documents with date field between start_date and end_date
    docs = collection.where('date', '>=', start_date).where('date', '<=', end_date).get()

    result = []
    # Iterate through the documents and extract the desired field
    for doc in docs:
        obj = {
            "date" : doc.to_dict()["Date"].strptime(start_date, '%Y-%m-%d'),
            "emotions" : doc.to_dict()["Keywords"].split("|")
            
        }
        result.append(obj)

    print(result)  