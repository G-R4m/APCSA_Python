def grapevines():
    
    R = int(input("enter the length of the row, in feet "))
    E = int(input("enter the the amount of space, in feet, used by an end-post assembly "))
    S = int(input("enter the space between vines, in feet row "))
    
    V = (R - (2 * E)) / S
    
    print("You will be able to have", V, "grapevines that wil fit in each row")

grapevines() 
    
    
