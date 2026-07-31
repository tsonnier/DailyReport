# main.py
# Main function, calls other functions
# Designed to be called once per day, will email if 

# Currently working on threshold
import os
from dotenv import load_dotenv

import emailer
import rates
from calculator import calculate_remaining_balance,get_closing_costs,get_savings

THRESHOLD = float(os.getenv("MORTGAGE_INTEREST_RATE")) - 0.5

def main():
    load_dotenv()
    principal = os.getenv("MORTGAGE_START_AMOUNT")
    


    rate_pair = rates.get_curr_mortgage_rates("MORTGAGE30US", True)
    curr_rate = rate_pair[1]
    print("Current Rate: " + str(curr_rate))
    print("Rate Threshold: " + str(THRESHOLD))
    if(curr_rate < THRESHOLD):
        #print("New Rate is Lower!!!!!")
        subject="Mortgage Tracker: New Rate!"
        message="You've got a new low rate! Rate = " + str(curr_rate)
        emailer.send_email(subject, message)
    else:
        print("New rate is not low enough, hold.")


    pass

main()
