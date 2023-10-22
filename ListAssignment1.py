sale_list = []
sum = 0

for count in range(7):
    print("Please enter the store sale's for day", count + 1, "of the week:")
    store_input = float(input())
    sale_list.append(store_input)
    sum = sum + sale_list[count]
  
print("This week's total sales is: $", sum)