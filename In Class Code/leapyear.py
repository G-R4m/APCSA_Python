def lpyr():
    i = int(input("Do you want to play game? /n (0=YES, 1=NO) "))
    
    #redundance to avoid having incorrect choise as input
    # "!" means "not"
    
    while i!=0 and i!=1:
        i = int(input("Do you want to play game? /n (0=YES, 1=NO)" ))
        
    while i!=1:
        print("Type in a year and the program will determine")
        yr = int(input("if the yearr is a leap year"))
        
        if (yr % 400 == 0) or (yr % 4 == 0 and yr % 100 != 0):
            print ("LEAP YEAR")
            print ("YOU WON THE GAME")
            
        else:
            print ("Not a leap year")
            
        i = int(input("Again? (0=YES, 1=NO) "))
        
lpyr()