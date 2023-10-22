def main():
    numb_emp = numb_get() 
    total_days = days(numb_emp) 
    absence = average(numb_emp, total_days) 

    print("The average absence is:", absence)

def numb_get():
 numb_emp = int(input("Please enter the number of employees: "))
 while(numb_emp < 1):
    numb_emp = int(input("Error, invalid response. Employees cannot be less than 1. Please try again!: "))
 return numb_emp

def days(numb_emp):
    total = 0
    for n in range(numb_emp):
     print("Enter the number of absences for employee #", n + 1, ":")
     absence = int(input())
     while(absence < 0): 
        absence = int(input("Error, invalid response. Absences cannot be negative. Please try again!: "))
     total = total + absence 
    return total

def average(numb_emp, total_days):
    return (total_days/numb_emp) 

main()