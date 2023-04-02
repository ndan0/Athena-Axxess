import fitbit
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
import datetime

client = fitbit.Fitbit(
    os.getenv("CLIENT_ID"), 
    os.getenv("CLIENT_SECRET"),
    access_token='eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1FRWlEiLCJzdWIiOiI3N0JDOUQiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd3BybyB3bnV0IHdzbGUgd3dlaSB3c29jIHdhY3Qgd3NldCB3bG9jIiwiZXhwIjoxNjgwNDUzNjkzLCJpYXQiOjE2ODA0MjQ4OTN9.QaG3YJj-Y9gHxCDpTTW7EDV_43gOPS9PyhF1UemqmY0', 
    refresh_token='e27dbea10de1566b60263e323b8f4ced1942069b50aac5083f529f5170d2de5e'
)

def get_heart_rate(start_date, num_of_day):
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
        avg_heart.append(obj)

    print(avg_heart)
    return avg_heart


# get_heart_rate('2023-01-01', 7)