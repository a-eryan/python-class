REGULAR_GAS = 2.89 #Variable R
PLUS_GAS = 3.09 #Variable P
SUPER_GAS = 3.39 #Variable S
total_wash = 0

selection_gallons = float(input('Please enter the number of gallons: '))
selection_gas = (input('Enter gas type (R, P, S, or N): '))
selection_carwash = (input('Enter Y or N for car wash: '))

print('**************************************\n*                                    *\n*                                    *')
print('*     Gas-N-Clean Service Station    *')
print('*                                    *')
print('*       October 3, 2022              *')
print('*                                    *')
print('**************************************')
if selection_gas == 'R': #Regular==============================================================
    total_gas = selection_gallons * REGULAR_GAS
    if selection_carwash == 'Y':
        if total_gas >= 10:
            total_wash = 1.25 
            print ('Amount Gasoline purchases\t',selection_gallons, 'Gallons')
            print ('Price per gallons\t$',REGULAR_GAS)
            print('Total gasoline purchases\t$'+format(total_gas,'.2f'))
            print ('Car wash cost\t$',total_wash)
            total_due = total_gas + total_wash
            print ('Total due\t$'+format(total_due,'.2f'))
        if total_gas < 10:
            total_wash = 3
            print ('Amount Gasoline purchases\t',selection_gallons)
            print ('Price per gallons\t$',REGULAR_GAS)
            print ('Total gasoline purchases\t$'+format(total_gas,'.2f'))
            print ('Car wash cost\t$',total_wash)
            total_due = total_gas + total_wash
            print ('Total due\t$'+format(total_due, '.2f'))
    if selection_carwash == 'N':
        total_wash = 0
        print ('Amount Gasoline purchases\t',selection_gallons)
        print ('Price per gallons\t$',REGULAR_GAS)
        print ('Total gasoline purchases\t$'+format(total_gas,'.2f'))
        print ('Car wash cost\t$',total_wash)
        total_due = total_gas + total_wash
        print ('Total due\t$'+format(total_due, '.2f'))
if selection_gas == 'P': #Plus==============================================================
    total_gas = selection_gallons * PLUS_GAS
    if selection_carwash == 'Y':
        if total_gas >= 10:
            total_wash = 1.25 
            print ('Amount Gasoline purchases\t',selection_gallons, 'Gallons')
            print ('Price per gallons\t$',PLUS_GAS)
            print('Total gasoline purchases\t$'+format(total_gas,'.2f'))
            print ('Car wash cost\t$',total_wash)
            total_due = total_gas + total_wash
            print ('Total due\t$'+format(total_due,'.2f'))
        if total_gas < 10:
            total_wash = 3
            print ('Amount Gasoline purchases\t',selection_gallons)
            print ('Price per gallons\t$',PLUS_GAS)
            print ('Total gasoline purchases\t$'+format(total_gas,'.2f'))
            print ('Car wash cost\t$',total_wash)
            total_due = total_gas + total_wash
            print ('Total due\t$'+format(total_due, '.2f'))
    if selection_carwash == 'N':
        total_wash = 0
        print ('Amount Gasoline purchases\t',selection_gallons)
        print ('Price per gallons\t$',PLUS_GAS)
        print ('Total gasoline purchases\t$'+format(total_gas,'.2f'))
        print ('Car wash cost\t$',total_wash)
        total_due = total_gas + total_wash
        print ('Total due\t$'+format(total_due, '.2f'))
if selection_gas == 'S': #Super==============================================================
    total_gas = selection_gallons * SUPER_GAS
    if selection_carwash == 'Y':
        if total_gas >= 10:
            total_wash = 1.25 
            print ('Amount Gasoline purchases\t',selection_gallons, 'Gallons')
            print ('Price per gallons\t$',SUPER_GAS)
            print('Total gasoline purchases\t$'+format(total_gas,'.2f'))
            print ('Car wash cost\t$',total_wash)
            total_due = total_gas + total_wash
            print ('Total due\t$'+format(total_due,'.2f'))
        if total_gas < 10:
            total_wash = 3
            print ('Amount Gasoline purchases\t',selection_gallons)
            print ('Price per gallons\t$',SUPER_GAS)
            print ('Total gasoline purchases\t$'+format(total_gas,'.2f'))
            print ('Car wash cost\t$',total_wash)
            total_due = total_gas + total_wash
            print ('Total due\t$'+format(total_due, '.2f'))
    if selection_carwash == 'N':
        total_wash = 0
        print ('Amount Gasoline purchases\t',selection_gallons)
        print ('Price per gallons\t$',SUPER_GAS)
        print ('Total gasoline purchases\t$'+format(total_gas, '.2f'))
        print ('Car wash cost\t$',total_wash)
        total_due = total_gas + total_wash
        print ('Total due\t$'+format(total_due, '.2f'))
if selection_gas == 'N':
        print ('Amount Gasoline purchases\t0')
        print ('Price per gallons\t$0.00')
        print ('Total gasoline purchases\t$0.00')
        print ('Car wash cost\t$3.00')
        print ('Total due\t$3.00')   
print('Thank you for stopping\nPlease come again\nRemember to buckle up and drive safely')

 