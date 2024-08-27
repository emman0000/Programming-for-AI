
#task 1 calculate area 

def area(length, width):
    return length * width

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

my_area = area(length, width)
print("Area: ", my_area)
