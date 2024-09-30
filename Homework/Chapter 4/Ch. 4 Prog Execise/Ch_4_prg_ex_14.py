def pat():
    
    r = int(input("How much rows do you want to have?: "))
    print()
    
    for i in range(1, r+1):
        
        print("*" * r)
        
        r -= 1
        
pat()