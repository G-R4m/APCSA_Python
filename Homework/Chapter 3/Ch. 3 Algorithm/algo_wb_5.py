def idk():
    
    amount1 = int(input("please enter 1st number: "))
    amount2 = int(input("please enter 2nd number: "))
    
    if amount1 > 10 and amount2 < 100:
        if amount1 > amount2:
            print("it seems that", amount1, "is greater than", amount2)
        else:
            print ("it seems that", amount2, "is greater thatn", amount1)
    
    else:
        print()
        print()
        print("please try again!")
        print()
        print("Please make sure 1st # is greater than 10")
        print("Also make sure that 2nd # is less that 100")
        
idk()
    