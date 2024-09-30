def pp():
    x = int(input("Enter a number less than 100: "))
    print(x)
    
    if x < 100:
        
        product = x
        
        while product < 100:
            product = product * 10
            
            print(product)
        
    else:
        print("invalid number")
    
    
    
pp()