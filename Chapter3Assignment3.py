print('Welcome to the savings account balance program!')

annual_interest = float(input('Please enter the annual interest rate: '))
while(annual_interest < 0):
    annual_interest = float(input('Error. Please re-enter the annual interest rate: '))
starting_balance = float(input('Please enter the starting balance: '))
months_passed = int(input('Please enter the total months that have passed: '))
while(months_passed < 0):
    months_passed = int(input('Error. Please re-enter the total months that have passed:'))

#innitalize variables for the for loop
monthly_int = annual_interest/12 
total_deposit = 0
total_withdraw = 0
total_int = 0

for i in range(months_passed):
    print('Month ', i+1, ' Statement')
    month_depo = float(input('Please enter the money deposited into the account for that month: '))
    while(month_depo < 0):
        month_depo = float(input('Error. Please re-enter the money deposited: '))
    total_deposit += month_depo
    starting_balance += month_depo
    withdraw = float(input('Please enter the amount of money withdrawn: '))
    while(withdraw < 0):
        withdraw = float(input('Error. Please re-enter the total amount of money withdrawn: '))
    starting_balance -= withdraw #substracting the withdrawn from the total balance
    total_withdraw += withdraw #adds withdrawn from the total balance 
    interest = monthly_int * starting_balance #finds the current interest for that month
    total_int += interest #adds current monthly interest to the total INTEREST
    starting_balance += interest #adds current monthly interest to the total BALANCE 

print('Remaining balance: $'+format(starting_balance, '.2f'))
print('Total amount deposited: $'+format(total_deposit, '.2f'))
print('Total amount withdrawn: $'+format(total_withdraw, '.2f'))
print('Total amount of interest: $'+format(total_int, '.2f'))
