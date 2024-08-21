# Task 4
num_list = input("ENTER THE NUMBERS YOU WISH TO ADD: ")
sum =0

for num in num_list.split():
    sum += int(num)
   
print(sum)
