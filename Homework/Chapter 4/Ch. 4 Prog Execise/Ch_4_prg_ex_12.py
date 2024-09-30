def factorial():
    n = int(input("enter a non negative integer: "))
    result = 1 
    for i in range (2, n+1):
        result *= i
        
        print(i)
        
    print(n,"! =", result)

factorial()