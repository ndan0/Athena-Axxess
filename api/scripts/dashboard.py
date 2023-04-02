import firebase_admin
from datetime import datetime, timedelta
from firebase_admin import credentials, firestore

db = firestore.client()  # this connects to our Firestore database
collection = db.collection('query-db')  # opens 'query-db' collection

def get_emotion(start_dt, num_of_days):
    # Define number of days to add to start date
    n_days = num_of_days

    # Calculate end date
    start_date = datetime.strptime(start_dt, '%Y-%m-%d')
    # start_ts = start_date.timestamp()
    end_date = start_date + timedelta(days=n_days)
    end_dt = datetime.strftime(end_date, '%Y-%m-%d')
    print(start_dt)
    print(end_dt)
    # Query documents with date field between start_date and end_date
    docs = collection.where('Date', '>=', start_dt).where('Date', '<=', end_dt).get()

    result = []
    # Iterate through the documents and extract the desired field
    for doc in docs:
        print("doc", doc.to_dict())
        obj = {
            "date" : doc.to_dict()["Date"],
            "emotions" : doc.to_dict()["Sentiment"]
            
        }
        result.append(obj)

    print(result)   
    return result

def get_keywords(start_dt, num_of_days):
    print("hi")
    # Define number of days to add to start date
    n_days = num_of_days

    # Calculate end date
    start_date = datetime.strptime(start_dt, '%Y-%m-%d')
    # start_ts = start_date.timestamp()
    end_date = start_date + timedelta(days=n_days)
    end_dt = datetime.strftime(end_date, '%Y-%m-%d')
    print(start_dt)
    print(end_dt)
    # Query documents with date field between start_date and end_date
    docs = collection.where('Date', '>=', start_dt).where('Date', '<=', end_dt).get()

    result = []
    # Iterate through the documents and extract the desired field
    for doc in docs:
        print("doc", doc.to_dict())
        obj = {
            "date" : doc.to_dict()["Date"],
            "keywords" : doc.to_dict()["Keywords"]
            
        }
        result.append(obj)

    return result