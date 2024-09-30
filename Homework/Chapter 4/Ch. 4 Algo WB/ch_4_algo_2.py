def sum():
    i = 1
    while i != 0:
        x = int(input("Please enter any number! "))
        y = int(input("Enter another number! "))
        
        print()
        print("Your numbers", x, "and", y, "equals to:", x + y)
        print()
        
        i = int(input("Do you want to add more? Press '0' if no: "))
        print()
sum()
    