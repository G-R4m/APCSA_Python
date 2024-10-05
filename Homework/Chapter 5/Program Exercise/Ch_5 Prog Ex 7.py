def seating():
    class_a = int(input("Please enter the tickets sold for Class A tickets: "))
    class_b = int(input("Please enter the tickets sold for Class B tickets: "))
    class_c = int(input("Please enter the tickets sold for Class C tickets: "))
    
    total = (class_a * 20) + (class_b * 15) + (class_c * 10)
    
    print()
    print("The total amount of income generated from ticket sales is: $", total)
    
    
    
seating()