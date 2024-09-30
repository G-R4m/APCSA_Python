def v():
    s = int(input("How fast is your car going? (mph): "))
    t = int(input("How many hours is it going that speed? "))
    c = 0
    
    print()
    print("Hour:			Distance Traveled:")
    print("__________________________________________")
    
    while c < t:
        c += 1
        
        print("  ",c, "			", (s * c), "miles! :O")
    
       
v()