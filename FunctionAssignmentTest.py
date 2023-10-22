def get_number():
    print('Please enter the number of employees:')
    number_of_employees = int(input())
    if number_of_employees >= 1:
        return number_of_employees
    while number_of_employees < 1:
        print('Error, invalid response. Employees cannot be less than 1')
        number_of_employees = int(input('Please enter the number of employees:'))

def total_days(number_of_employees):
    sum = 0
    for n in range(number_of_employees):
     print('Please enter the absence for employee #', n + 1)
     absent = int(input())
     while absent < 0:
        print('Error, absences cannot be negative.')
        absent = int(input())
     sum = sum + absent
     return sum
 


def average(number_of_employees,sum_of_days):
 return (sum_of_days/number_of_employees)#returned the avg number of absent days
    
def main():
    number_of_employees = get_number()#calling get_number function
    sum_of_days = total_days(number_of_employees)#calling total_days function #calling average function
    avg_days_absent = average(number_of_employees, sum_of_days)
    print(avg_days_absent)#printed average absent days of an employee in main method

 
main()#calling main function