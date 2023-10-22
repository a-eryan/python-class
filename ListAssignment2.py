import random
lottery_list = []



for count in range(7):
        generator = random.randrange(0,10)
        lottery_list.append(generator)


index = 1
for lottery_list in lottery_list:
        print("Number", (index), "of your lottery ticket is: ",(lottery_list))
        index += 1