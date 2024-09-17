def num():
    x = int(input("Please input any integer of your choosing! "))
    
    if x > 0:
        print("Your number is positive! and.... ")
        
        if x % 2 == 0:
            print("it's also even :)")
            
        else:
            print("it's odd >:)")
            
    elif x == 0:
        print("Why did you choose 0? :(")
        
    else:
        print("You number is negatve! and.... ")
        
        if x % 2 == 0:
            print("it's also even :)")
            
        else:
            print("it's odd >:)")
        
    
        
num()
