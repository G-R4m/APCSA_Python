def rain():
    year = int(input("Please enter the number of years: "))
    print()
    
    c = 0
    
    inch = 0
    
    while c < year:
        
        c += 1
        
        for i in range(1, 13):
            
            print("For month", i,)
            
            inch = inch + float(input("please enter inches of rainfall: "))
            print()
            
    print()       
    print("Over", (year * 12), "Months, there was a total of", inch, "inches of rain!")
    print()
    print("Overall, there was an average rainfall of", (inch / (year * 12)))
    
    
    
    
rain()