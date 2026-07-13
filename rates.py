# rates.py
# Downloads today's mortgage rate
# Accesses the referenced online source for the nation's mortgage rate and returns that rate on demand.  
import requests
from fredapi import Fred
import os
from dotenv import load_dotenv

DEBUG = True


def get_curr_mortgage_rates():
    load_dotenv()
    series_id = "MORTGAGE30US"
    API_key = os.getenv("SECRET_KEY")

    fred = Fred(api_key=API_key)
    rate = fred.get_series_latest_release(series_id)
    print("Getting Data:" + str(rate.tail))
    

if DEBUG:
    get_curr_mortgage_rates()