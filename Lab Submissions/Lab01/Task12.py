
dictionary ={}

for num in range(1,16): #I have to start at 1 and end at 16 to include 15
  dictionary[num] = num**2



print("Number : Squared")
for key, value in dictionary.items():
   print(f"{key} : {value}" )
