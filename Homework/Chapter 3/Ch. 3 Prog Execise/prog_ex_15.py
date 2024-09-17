def time():
    s = int(input("please enter any number of seconds: "))
    
    if s < 60:
        
        print("there are", s, "seconds")
    
    else:
        if s >= 60 and s <= 3599:
            
            m = s // 60
            
            ts = s % 60
            
            print("there are", m, "minutes, and", ts, "seconds")
            
        elif s >= 3600 and s <= 86399:
            
            h = s // 3600
            
            m = (s % 3600) // 60
            
            ts = s % 60
            
            print("there are", h, "hours,", m, "minutes, and", ts, "seconds")
            
        elif s >= 86400:
            
            d = s // 86400
            
            h = (s % 86400) // 3600
            
            m = (s % 3600) // 60
            
            ts = s % 60
            
            print("there are", d, "days", h, "hours,", m, "minutes, and", ts, "seconds")
    
    
         
    
     
time()