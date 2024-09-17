def feb():
   
    yr = int(input("Type in any 4 digit year: "))
        
    if (yr % 400 == 0) or (yr % 4 == 0 and yr % 100 != 0):
        print ("In", yr, "February has 29 days!")
            
    else:
        print ("In", yr, "February has 28 days")
            
feb()
    
    
  