def wheel():
    
    x = int(input("please enter a number from 0 to 36: "))
    
    if x < 0 or x > 36:
        print("You've inputed a wrong number, please try again")
        
    else:
        if x == 0:
            print("pocket is green")
            
        elif x <=10 and x >=1:
            
            if x % 2 == 0:
                print("Pocket is black")
                
            else:
                print("pocket is red")
                
        elif x <=18 and x >=11:
            
            if x % 2 == 0:
                print("Pocket is red")
                
            else:
                print("pocket is black")
                
        elif x <=28 and x >=19:
            
            if x % 2 == 0:
                print("Pocket is black")
                
            else:
                print("pocket is red")
                
        elif x <=36 and x >= 29:
            
            if x % 2 == 0:
                print("Pocket is red")
                
            else:
                print("pocket is black")
                
wheel()
            
    
              