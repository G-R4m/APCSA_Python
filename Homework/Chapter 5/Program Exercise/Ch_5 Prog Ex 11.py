import random

def math_test():
    
    for i in range(1, 6):
    
        print("Question", i)
        print()
        
        num1 = random.randint (1, 10)
        
        num2 = random.randint (1, 10)
        
        print(num1, "+", num2, "=", (num1 + num2))
        print()
        
    
math_test()
    

