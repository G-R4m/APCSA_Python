def main():
    x = int(input("Please enter 1st number you want to multiply by: "))
    y = int(input("Please enter 2nd number you want to multiply by: "))
    print()
    print("Using recursion, the answer is:",mult(x, y))
    print()
    print("The real answer is:", x * y)

def mult(x, y):
    if x == 0:
        return 0
    return y + mult(x - 1, y)
    
        
        
        
        
    
main()
