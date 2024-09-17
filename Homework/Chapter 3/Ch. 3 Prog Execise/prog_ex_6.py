def date():
    m = int(input("Please enter a month (January = 1, February = 2 and so on): "))
    print()
    d = int(input("Please enter a day for that month: "))
    print()
    y = int(input("Finally, please enter the last two digits of any year (2020 = 20 and so on): "))
    print()
    
    if m * d == y:
        print("No flipping way! Your date of", m, "/",d, "/", y, "is MAGIC!")
        
    else:
        print("Your date of" , m, "/",d, "/", y, "is not magic :(")
        
date()
    
    
    