def pop():
    p = int(input("Organisms you're starting with: "))
    avg = float(input("Agerage daily increase (as a percentage): "))
    days = int(input("Number of days that will pass: "))
    print()
    
    print("Day Approximate:	Population:")
    print()
    
    for i in range (1, days + 1):
        
        print(i, "			", p)
        
        p += p * (avg * 0.01)
        
pop()

