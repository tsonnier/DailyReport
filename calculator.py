# calculator.py
# Calculates the amount saved in a hypothetical refinance

from datetime import date
from datetime import datetime
#from dateutil import relativedelta

DEBUG = True

def get_savings(balance, curr_rate, new_rate, years):
    # Get the current mortgage data 
    # Get latest interest rate
    # Calculate amount saved 

    old_monthly_payment = monthly_payment(balance, curr_rate, years)
    new_monthly_payment = monthly_payment(balance, new_rate, years)

    return old_monthly_payment - new_monthly_payment
    pass

def monthly_payment(balance, annual_rate, years):
    """
    Calculates the expected monthly payment using 
    :param balance: float - the current balance for the loan
    :param annual_rate: float - the annual interest rate, expressed as a percentage (5% interest = 5.0 value)
    :param years: int - the number of years the loan applies to (30 year loan, etc)

    """
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

def get_months_difference(loan_start_date):
    curr_date = date.today()

    start_date_text = loan_start_date
    date_format = "%m/%d/%Y"
    start_date = datetime.strptime(start_date_text, date_format).date()

    time_difference_months = (curr_date.year - start_date.year) * 12 + (curr_date.month - start_date.month)
    print(time_difference_months)    


def get_closing_costs(balance):
    """
    Returns the estimated closing costs for a loan given the current balance
    Estimated closing costs go from 2%-5% of loan.  Assume 5%
    """
    return (balance * 0.05)

def break_even_time(balance, curr_rate, new_rate, years):
    savings_per_month = get_savings(balance, curr_rate, new_rate, years)
    closing_costs = get_closing_costs(balance)
    return closing_costs / savings_per_month

if DEBUG:
    print("Calculate Remaining Balance Test")
    print(calculate_remaining_balance(277147, 5.999, 30, 14))
    print("Monthly Payment Test 1")
    print(monthly_payment(277147, 5.999, 30))
    print("Monthly Payment Test 2")
    print(monthly_payment(277147, 4.999, 30))
    print("Get Closing Costs Test")
    print(get_closing_costs(277147))
    print("Get Savings Test")
    print(get_savings(277147, 5.999, 4.999, 30))
    print("Get Break Even Time")
    print(break_even_time(277147, 5.999, 4.999, 30))