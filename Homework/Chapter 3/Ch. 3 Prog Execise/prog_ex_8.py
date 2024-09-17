def hotdog():
    people = int(input("Please enter the ammount of people going: "))
    hd = int(input("how many hotdogs will one person be getting? "))
    
    total = people * hd
    
    buns = 8
    pack = 10
    
    pn = total // pack
    bn = total // buns
    lefthd = pack - (total % pack)
    leftbun = buns - (total % buns)
    
    print("Minimum number of hot dog packs needed is", pn)
    print("Minimum number of buns needed is", bn)
    print("Number of hot dogs left is", lefthd)
    print("Number of hot dog buns left is", leftbun)
    
hotdog()
    
    
   
        
    
    
                 