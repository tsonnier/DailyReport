# rates.py
# Downloads and returns mortgage rates from the Federal Reserve Bank (FRED)
# Accesses the referenced online source for the nation's mortgage rate and returns that rate on demand.  
import requests
from fredapi import Fred
import os
from dotenv import load_dotenv

DEBUG = False

# Series IDs for mortgage types
MORT30YEAR = "MORTGAGE30US" # 30 year fixed rate mortgage
MORT15YEAR = "MORTGAGE15US" # 15 year fixed rate mortgage
MORT5Year = "MORTGAGE5US" # 5 year adjustable rate mortgage


def get_curr_mortgage_rates(series_id, latest=False):
    # Returns full rate object
    # Date - rate.axes[0][index], rate - rate.array[index]

    load_dotenv()
    API_key = os.getenv("FRED_SECRET_KEY")

    fred = Fred(api_key=API_key)
    rate = fred.get_series_latest_release(series_id)
    #latest_rate = rate.array[rate.array.size-1]
    #print("Getting Data: " + str(latest_rate))
    list_size = rate.array.size-1
    #print("Date: " + str(rate.axes[0][list_size]) + ", Rate: " + str(rate.array[list_size]))
    if(latest):
       
       return [rate.axes[0][list_size], rate.array[list_size] ]
    else:
        return rate


def get_all_mortgage_rates():
    rate_30_year = get_curr_mortgage_rates(MORT30YEAR)
    rate_15_year = get_curr_mortgage_rates(MORT15YEAR)
    pass

if DEBUG:
    get_curr_mortgage_rates("MORTGAGE30US", True)