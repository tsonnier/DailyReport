# calculator.py
# Calculates the amount saved in a hypothetical refinance

from datetime import date
from datetime import datetime
#from dateutil import relativedelta

def get_savings():
    # Get the current mortgage data 
    # Get latest interest rate
    # Calculate amount saved 
    pass

def monthly_payment(balance, annual_rate, years):
    monthly_rate = annual_rate / 100 / 12
    months = years * 12

    return (
        balance
        * monthly_rate
        * (1 + monthly_rate) ** months
        / ((1 + monthly_rate) ** months - 1)
    )

def calculate_remaining_balance(principal, annual_rate, total_years, payments_made):
    """
    Calculates the remaining mortgage balance using the standard amortization formula.
    
    :param principal: float - The original loan amount (e.g., 300000)
    :param annual_rate: float - The annual interest rate as a decimal (e.g., 0.06 for 6%)
    :param total_years: int - The total lifespan of the mortgage in years (e.g., 30)
    :param payments_made: int - The number of monthly payments completed (e.g., 120 for 10 years)
    :return: float - The remaining balance on the mortgage
    """
    # Convert annual interest rate to a monthly rate
    r = annual_rate / 12
    
    # Convert total years to total number of monthly payments
    n = total_years * 12
    
    # Variable 'p' for payments made
    p = payments_made
    
    # Handle the edge case of a 0% interest rate to avoid division by zero
    if r == 0:
        return principal * (1 - (p / n))
        
    # Apply the remaining balance formula
    balance = principal * (((1 + r)**n - (1 + r)**p) / ((1 + r)**n - 1))
    
    return round(balance, 2)

def get_current_balance(start_bal, monthly_payment, start_date):
    curr_date = date.today()

    start_date_text = start_date
    date_format = "%m/%d/%Y"
    start_date = datetime.strptime(start_date_text, date_format).date()

    time_difference_months = (curr_date.year - start_date.year) * 12 + (curr_date.month - start_date.month)
    print(time_difference_months)
    


    #curr_bal = start_bal - (monthly_payment * (time_difference_months - 1)) + 
    #print(curr_bal)

#get_current_balance(281250, 1686.06, "04/28/2025")
#print(calculate_remaining_balance(281250, .05999, 30, 14))