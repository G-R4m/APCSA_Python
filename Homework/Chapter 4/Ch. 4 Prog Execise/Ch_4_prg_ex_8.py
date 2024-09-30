def word():
     c = 1
     num = -1
     letters = 0
     while c != 0:
         
         num += 1 
         
         word = input("please enter any word or enter nothing to stop: ")
         print()
         
         letters = letters + len(word) #len() is to count the number of characters in a string in Python
                                       #(Idk, i searched it up on google)
        
         
         if word == "":
             
             c = 0
             
             print()
             print("You have typed", num, "words!")
             print("The average length of all your words is:", (letters//num), "letters!")
word()