import fitbit
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
import datetime

client = fitbit.Fitbit(
    os.getenv("CLIENT_ID"), 
    os.getenv("CLIENT_SECRET"),
    access_token='eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1FRWlEiLCJzdWIiOiI3N0JDOUQiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd3BybyB3bnV0IHdzbGUgd3dlaSB3c29jIHdhY3Qgd3NldCB3bG9jIiwiZXhwIjoxNjgwNDQ4NjkwLCJpYXQiOjE2ODA0MTk4OTB9.v7YBveKjMGeSbexRm2xQi27X9wCpZQqqJLIFVdLXKOA', 
    refresh_token='65a396c8268390200b62b60698a02925db91db013b204213f027bb86bd9f6dc2'
)

def get_heart_rate(start_date, num_of_day):
    # Set the start date and end date for the heart rate data
    start = datetime.datetime.strptime(start_date, '%Y-%m-%d')

    avg_hr = []
    avg_heart = []

    for i in range(num_of_day):
        date = start + datetime.timedelta(days=i)
        data = client.intraday_time_series('activities/heart', base_date=date.strftime('%Y-%m-%d'), detail_level='1sec')
        hr_list = [hr['value'] for hr in data['activities-heart-intraday']['dataset']]
        if hr_list:
            avg_hr.append(sum(hr_list)/len(hr_list))
        else:
            avg_hr.append(0)
        obj = {
            "date": date.strftime('%Y-%m-%d'),
            "avg_hrt": avg_hr
        }
        avg_heart.append(obj)

    print(avg_heart)