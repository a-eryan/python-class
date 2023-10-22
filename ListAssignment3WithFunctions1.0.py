hi = 5
hi2 = 3

print (hi + hi2)



def main():
 rainfall_list = []
 total = 0


 for count in range(12):
        print('Please enter the total amount of rainfall for month', count +1,':')
        rainfall = float(input())
        rainfall_list.append(rainfall)
 
 add()
 avg()
 minfunction()
 maxfunction()



def add(total, rainfall_list, count): 
    total = total + rainfall_list[count]   
    print('The total sum of rainfall this year is:', total)

def avg(total, total_average):
    total_average = total/12
    print('The total average is:', total_average)

def minfunction(total, rainfall_list):
    lowest = min(rainfall_list)
    print('The lowest amount of rainfall is:', lowest)

def maxfunction(highest, rainfall_list):
    highest = max(rainfall_list)
    print('The highest amount of rainfall is:', highest)

main()