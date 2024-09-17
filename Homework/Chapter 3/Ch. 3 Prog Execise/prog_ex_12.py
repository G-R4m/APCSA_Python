def pack():
    n = int(input("Please enter the number of packaged purchased: "))
    p = n * 99
    
    if n < 10:
        print("no discout, thank you for your purchase")
        print("your total will be", p, "$")
    
    elif n >= 10 and n <= 19:
        d = 0.1
        
        print("10% discount! Thank you for your purchase")
        print("your total will be", p - (p * d) , "$")
    
    elif n >= 20 and n <= 49:
        d = 0.2
        
        print("20% discount! Thank you for your purchase")
        print("your total will be",p - (p * d) , "$")
    
    elif n >= 50 and n <= 99:
        d = 0.3
        
        print("30% discount! Thank you for your purchase")
        print("your total will be", p - (p * d) , "$")
        
    elif n >= 100:
        d = 0.4
        
        print("40% discount! Thank you for your purchase")
        print("your total will be", p - (p * d), "$")
    
    
    
    
pack()