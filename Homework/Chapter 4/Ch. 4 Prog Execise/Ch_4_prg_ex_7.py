def penny():
    
    p = 0.01
    day = int(input("Please enter the number of days you've had the magical penny: "))
    c = 0
    total = 0
    
    print()
    print("Day:					Money Earned:")
    print("________________________________________________________")
    print()
    
    while c < day:
        
        c += 1
        
        print(c, "						$", p)
        
        total = p + total
        
        p = p * 2
        
        
    print("________________________________________________________")
    
    print()
    
    print("Total money gathered: $", total)
    
    
    
penny()