#project Python from Leonard Blam and Ben Broder

import matplotlib.pyplot as plt
from colorama import Fore, Back, Style
import numpy as np
import numpy_financial as npf

def FV(present_value, interest_rate, num_payments):
    return (present_value * (pow((1+interest_rate), num_payments)-1) * (1+interest_rate)) / interest_rate

def future_value_of_payments(interest_rate):
    try:
        print(Fore.GREEN)
        num_payments = int(input("Enter the number of payments: "))
        present_value = float(input("Enter the present value: "))
        print(Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "Error: Please enter a valid number of payments and payment amount." + Style.RESET_ALL)
        future_value_of_payments(interest_rate)
   # print(Fore.BLUE + f'The future value of the payments is:{future_value}' + Style.RESET_ALL)
    # FV = []
    # last_future_value = present_value
    # for i in range(1, num_payments):
    #     present_value = last_future_value
    #     future_value = present_value * (1 + interest_rate /100)**num_payments
    #     FV.append(future_value)
    #     last_future_value = future_value
    # Plotting the graph
    values = {}
    for j in range(0, num_payments):
        values[j] = FV(present_value, interest_rate, j)
    x = list(range(0, num_payments))
    y = list(values.values())
        
    plt.plot(x, y)
    plt.xlabel("Payment Number")
    plt.ylabel("Future Value")
    plt.title("Future Value of Payments")
    plt.show()




def payments_against_loan(interest_rate):
    try:
        print(Fore.GREEN)
        loan_amount = float(input("Enter the loan amount: "))
        num_payments = int(input("Enter the number of payments: "))
        # payment_amount = loan_amount * interest_rate * (1 + interest_rate)**num_payments / ((1 + interest_rate)**num_payments - 1)
        print(Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "Error: Please enter a valid loan amount and number of payments." + Style.RESET_ALL)
        payments_against_loan(interest_rate)

    payment_amount = -1 * npf.pmt(interest_rate, num_payments, loan_amount)
    print(Fore.BLUE + f'The payment amount is: {payment_amount}' + Style.RESET_ALL)
    payment_left = FV(loan_amount, interest_rate, num_payments)
    print(payment_left)
    payments = []
    for i in range(0, num_payments):
        payments.append(payment_amount)
    x = [i for i in range(0, num_payments)]
    y = payments
    plt.plot(x, y)
    plt.xlabel("Duration of Loan (Months)")
    plt.ylabel("Payment Amount (Dollars)")
    plt.title("Payments Against Loan")
    plt.show()

def interest_portion_of_payment(interest_rate):
    try:
        print(Fore.GREEN)
        payment_amount = float(input("Enter the payment amount: "))
        # loan_amount = float(input("Enter the loan amount: "))
        num_payments = int(input("Enter the number of payments: "))
        print(Style.RESET_ALL) 
    except ValueError:
        print(Fore.RED + "Error: Please enter a valid payment amount and number of payments." + Style.RESET_ALL)
        interest_portion_of_payment(interest_rate)

    interest_portions = []
    for i in range(1, num_payments + 1):
        interest_portion = payment_amount * interest_rate * ((1 + interest_rate)**(num_payments - i) / (1 + interest_rate)**num_payments - 1)
        interest_portions.append(interest_portion)
    plt.plot(range(1, num_payments + 1), interest_portions)
    plt.xlabel("Payment Number")
    plt.ylabel("Interest Portion of Payment")
    plt.title("Interest Portion of Payment over Time")
    plt.show()

def rate_of_interest_per_period(interest_rate):
    try:
        print(Fore.GREEN)
        payment_amount = float(input("Enter the payment amount: "))
        loan_amount = float(input("Enter the loan amount: "))
        num_payments = int(input("Enter the number of payments: "))
        print(Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "Error: Please enter a valid payment amount, loan amount and number of payments." + Style.RESET_ALL)
        rate_of_interest_per_period(interest_rate)
    
    rate_of_interest = payment_amount * (1 + interest_rate)**num_payments / (loan_amount * (1 + interest_rate)**num_payments - payment_amount) - 1
    print(Fore.BLUE)
    print("The rate of interest per period is: %.2f" % rate_of_interest)
    print(Style.RESET_ALL)
    # Generate the graph
    x = [i for i in range(1, num_payments + 1)]
    y = [rate_of_interest for _ in range(num_payments)]
    plt.plot(x, y)
    plt.xlabel("Payment Number")
    plt.ylabel("Interest Rate")
    plt.title("Rate of Interest per Period")
    plt.show()

def display_menu():

    print(Fore.GREEN + "Select an option:")
    print(Fore.GREEN +"1. Future Value of a series of payments")
    print(Fore.GREEN +"2. Payments against loan including interest")
    print(Fore.GREEN +"3. The interest portion of a payment")
    print(Fore.GREEN +"4. Rate of interest per period")
    print(Fore.GREEN +"5. Quit")
    print(Style.RESET_ALL)

def main():
    print(Style.RESET_ALL)
    run = True
    interest_rate = 0.0
    print(Fore.BLUE)
    print("Welcome to the Loan Calculator")
    try:
        interest_rate = float(input("Enter the interest rate (as a decimal): "))
    except ValueError:
        print(Fore.RED + "Invalid interest rate. Disconnecting Application!")
        print(Style.RESET_ALL)
        return
    print(Style.RESET_ALL)
    while run:
        display_menu()
        print(Fore.RED)
        try:
            option = int(input("Enter your option: "))
        except ValueError:
            print("Invalid option. Disconnecting Application!")
            break
        print(Style.RESET_ALL)
        if option == 1:
            future_value_of_payments(interest_rate)
        elif option == 2:
            payments_against_loan(interest_rate)
        elif option == 3:
            interest_portion_of_payment(interest_rate)
        elif option == 4:
            rate_of_interest_per_period(interest_rate)
        elif option == 5:
            run = False
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

