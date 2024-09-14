#File: Karatsuba.py
#Student: Giancarlo Ramriez
#
#Date: Spetember 13, 2024
#This program will use a special case of the Karatsuba Multiplication process, which takes two 4-digit integers supplied by the user.
#The computer will us an algorithm which will match up to the actual answer of the two 4-digit numbers.
#GitHub: G-R4m

def yes():
    game = int(input("Enter 1 for minigame: "))
    if game == 1:
        kat()
    else:
        print("goodbye!")
    




def kat():
    print()
    n1 = int(input("Please enter a 4 digit number "))
    print()
    n2 = int(input("now please enter another 4 digit number "))
    print()
    print()
    a = n1 // 100
    b = n1 % 100
    c = n2 //100
    d = n2 % 100
    e = a * c
    f = b * d
    g = (a + b) * (c + d)
    h = g - (e + f)
    i = e * 10000
    j = h * 100
    k = i + j + f
    ans = n1 * n2
    
    
    
    print("Using my algorithm, i've come up with the answer", k)
    print()
    print("The actual answer is", ans, ",of course I was right! :)")
    
    
yes()
    
    

    
