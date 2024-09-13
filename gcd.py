def gcd(a,b):
    if a > b:
        small = b
        large = a
    
    else:
        small = a
        large = b
        
    r = large % small #this is the remainder
    
    while r > 0:
        print (large, small, r)
        large = small
        small = r
        r = small % r
    
    return small

print (gcd (12345,67890222))
        
        
        
   
    
