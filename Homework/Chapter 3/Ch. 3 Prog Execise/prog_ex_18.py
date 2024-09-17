def res():
    v = input("Is anyone in your party vegetarian? ")
    vg = input("Is anyone in your party vegan? ")
    g = input("Is anyone in your party gluten-free? ")

    if v == "yes":
        
        if vg == "yes":
            
            if g == "yes":
                print("You are able to go to:")
                print("Corner Cafe and The Chef's Kitchen!")
            
            elif g == "no":
                print("You are able to go to:")
                print("Corner Cafe and The Chef's Kitchen!")
        
        elif vg == "no":
            
            if g == "yes":
                print("You are able to go to:")
                print("Corner Cafe, Main Street Pizza Company, and The Chef's Kitchen!")
            
            elif g =="no":
                
                print("You are able to go to:")
                print("Corner Cafe, Main Street Pizza Company, The Chef's Kitchen, and Mama's Fine Italian!")
                
    elif v == "no":
        if vg == "yes":
            
            if g == "yes":
                print("You are able to go to:")
                print("Corner Cafe and The Chef's Kitchen!")
            
            elif g =="no":
                print("You are able to go to:")
                print("Corner Cafe and The Chef's Kitchen!")
        
        elif vg == "no":
            
            if g == "yes":
                print("You are able to go to:")
                print("Corner Cafe, Main Street Pizza Company, and The Chef's Kitchen!")
            
            elif g =="no":
                print("You are able to go to:")
                print("Joe's Gourmet Burgers, Corner Cafe, Main Street Pizza Company, The Chef's Kitchen, and Mama's Fine Italian!")
    else:
        print("Make sure to have no Capitals in your response! Or you have an invalid response!")
                
    
                
res()

