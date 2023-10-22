def get_number():
    numb_of_employees= int(input('Please enter the number of employees:'))
    while numb_of_employees < 1:
        print('Error, invalid response. Employees cannot be less than 1')
        numb_of_employees = int(input('Please enter the number of employees:'))
   
def total_days(numb_of_employees):
     for n in range(numb_of_employees):
        total = 0
        print('Please enter the absence for employee #', n +1)
        absence =  int(input())
        while absence < 0:
            print('Error, invalid response. Absences cannot be less than 0. Please re-enter for employee #', n+1)
            absence =  int(input())
        total = total + absence
        return total
            
def average(number_of_employees,sum_of_days):
    return (sum_of_days//number_of_employees)


def main():
    number_of_employees = get_number()
    sum_of_days = total_days(number_of_employees)
    avg_days_present = average(number_of_employees, sum_of_days)
    print('The average is ', avg_days_present)

if __name__ == "__main__":
    main()
