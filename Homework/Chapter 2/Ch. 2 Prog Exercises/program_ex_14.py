def comp():
    
    P = int(input("The amount of principal originally deposited into the account the account ")) 
    r = float(input("please enter the annual interest rate paid by the account "))
    n = int(input("please enter the number of times per year that the interest is compounded, For example, if interest  is compounded monthly, enter 12. If interest is compounded quarterly, enter 4. "))
    t = int(input("The number of years the account will be left to earn interest "))
    
    A = P * (1 + (r / n)) ** (n * t)
    
    print("The amount of money that will be in the account after", t, "years, is", A)
    
comp()
