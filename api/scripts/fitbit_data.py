import fitbit
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
import datetime

client = fitbit.Fitbit(
    os.getenv("CLIENT_ID"), 
    os.getenv("CLIENT_SECRET"),
    access_token=os.getenv("FITBIT_ACCESS_KEY"), 
    refresh_token=os.getenv("FITBIT_REFRESH_TOKEN"),
)

def get_heart_rate(start_date, num_of_day):
    print("heart!")
    # Set the start date and end date for the heart rate data
    start = datetime.datetime.strptime(start_date, '%Y-%m-%d')

    # avg_hr = []
    avg_heart = []

    for i in range(num_of_day):
        date = start + datetime.timedelta(days=i)
        data = client.intraday_time_series('activities/heart', base_date=date.strftime('%Y-%m-%d'), detail_level='1sec')
        hr_list = [hr['value'] for hr in data['activities-heart-intraday']['dataset']]
        if hr_list:
            avg_hr = (sum(hr_list)/len(hr_list))
        else:
            avg_hr = (0)
        obj = {
            "date": date.strftime('%Y-%m-%d'),
            "avg_hrt": avg_hr
        }
        print(obj)
        avg_heart.append(obj)

    print(avg_heart)
    return avg_heart

def get_calories(start_date, num_of_day):
    # Set the start date and end date for the heart rate data
    start = datetime.datetime.strptime(start_date, '%Y-%m-%d')

    # avg_hr = []
    avg_heart = []

    for i in range(num_of_day):
        date = start + datetime.timedelta(days=i)
        date_str = date.strftime('%Y-%m-%d')
        calories = client.activities(date=date_str)['summary']['caloriesOut']
        obj = {
            "date": date.strftime('%Y-%m-%d'),
            "calories": calories
        }
        avg_heart.append(obj)

    print(avg_heart)
    return avg_heart


# get_heart_rate('2023-01-01', 7)