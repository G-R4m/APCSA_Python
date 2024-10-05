def shout():
    shouting = input("Type in any word: ")
    print()
    
    ord(shouting)
    a = ((ord(shouting) - 32))
    
    print(chr(a))
    
    
    print()
    print(shouting.upper(), end= "!")
    
shout()