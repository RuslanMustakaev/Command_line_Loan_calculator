import argparse
import math

parser = argparse.ArgumentParser(description="This program calculate credit based on data \
which you will input")

parser.add_argument("--type", choices=["annuity", "diff"],
                    help="You need to choose type of payment from list")
parser.add_argument("--payment", help="Enter monthly payment, except if you choose differentiated payments")
parser.add_argument("--principal", help="Enter principal value")
parser.add_argument("--periods", help="Is the number of months needed to replay the loan")
parser.add_argument("--interest", help="Enter interest value")

args = parser.parse_args()
data_from_user = [args.type, args.payment, args.principal, args.periods, args.interest]
data_test_list = [i for i in data_from_user if i is not None]  # For testing that entered data is enough for calculation
payment_type = args.type
payment = args.payment
principal = args.principal
periods = args.periods
interest = args.interest


def months_numbers():
    P = float(principal)
    A = float(payment)
    i = float(interest) / (12 * 100)
    n = math.ceil(math.log(A / (A - (i * P)), 1 + i))
    years = math.floor(n / 12)
    months = n - (years * 12)
    overpayment = int((A * n) - P)
    if n < 12:
        print(f"It will take {n} months to repay this loan!")
    elif n == 12:
        print("It will take 1 year to repay this loan!")
    elif months == 0:
        print(f"It will take {years} years to repay this loan!")
    else:
        print(f"It will take {years} years and {months} months to repay this loan!")
    print(f"Overpayment = {overpayment}")


def annuity_payment():
    P = float(principal)
    n = float(periods)
    i = float(interest) / (12 * 100)
    A = math.ceil(P * i * ((1 + i) ** n) / (((1 + i) ** n) - 1))
    overpayment = int((A * n) - P)
    print(f"Your annuity payment = {A}!")
    print(f"Overpayment = {overpayment}")


def loan_principal():
    A = float(payment)
    n = float(periods)
    i = float(interest) / (12 * 100)
    P = math.floor(A / ((i * ((1 + i) ** n)) / (((1 + i) ** n) - 1)))
    overpayment = int((A * n) - P)
    print(f"Your loan principal = {P}!")
    print(f"Overpayment = {overpayment}")


def diff_payment():
    n = int(periods)
    P = float(principal)
    i = float(interest) / (12 * 100)
    total_payment = 0
    for m in range(1, n + 1):
        D_m = math.ceil((P / n) + i * (P - (P*(m - 1)/n)))  # Monthly differentiated payment
        print(f"Month {m}: payment is {D_m}")
        total_payment += D_m
    overpayment = int(total_payment - P)
    print()
    print(f"Overpayment = {overpayment}")


for data in data_test_list:
    if "-" in data:
        print("Incorrect parameters")
        exit()
if len(data_test_list) < 4:
    print("Incorrect parameters")
elif payment_type == "diff" and payment is not None:
    print("Incorrect parameters")
elif interest is None:
    print("Incorrect parameters")
elif payment_type == "diff":
    diff_payment()
elif payment_type == "annuity":
    if principal is None:
        loan_principal()
    elif payment is None:
        annuity_payment()
    else:
        months_numbers()
