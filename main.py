# main.py
# Main function, calls other functions
# Designed to be called once per day, will email if 

# Currently working on threshold
import os
from dotenv import load_dotenv

import emailer
import rates
from calculator import calculate_remaining_balance,get_closing_costs,get_savings

THRESHOLD_30 = float(os.getenv("MORTGAGE_INTEREST_RATE")) - 0.5
THRESHOLD_15 = float(os.getenv("MORTGAGE_INTEREST_RATE")) - 1.0

def main():
    load_dotenv()
    principal = os.getenv("MORTGAGE_START_AMOUNT")


    rate_pairs = rates.get_all_mortgage_rates(True)
    
    curr_30_rate = rate_pairs[0][1]
    curr_15_rate = rate_pairs[1][1]
    print("Current 30 Year Rate: " + str(curr_30_rate))
    print("Current 15 Year Rate: " + str(curr_15_rate))
    print("Rate Threshold 30 Year: " + str(THRESHOLD_30))
    print("Rate Threshold 15 Year: " + str(THRESHOLD_15))
    if(curr_30_rate < THRESHOLD_30):
        #print("New Rate is Lower!!!!!")
        subject="Mortgage Tracker: New Rate!"
        message="You've got a new low rate! Rate = " + str(curr_rate)
        #emailer.send_email(subject, message)
    else:
        print("New rate is not low enough, hold.")


    pass

main()
