def grade():
    test1 = int(input("Please enter your grade for your first test, (should be at most 25 points): "))
    test2 = int(input("Please enter your grade for your second test, (should be at most 25 points): "))
    exam = int(input("Please enter your grade for your main exam, (should be at most 50 points): "))
    
    total = test1 + test2 + exam
    
    if test1 < 0 or test2 < 0 or exam < 0 or test1 > 25 or test2 > 25 or exam > 50:
        print("Error, you've input an impossible score. TRY AGAIN")
        
    else:
        if total >= 80:
            print("Grade is: Distinction")
        elif total < 50 or exam < 25:
            print("Grade is: Fail")
        elif total <=59 and total >= 50:
            print("Grade is: Pass")
        elif total < 80 and total >= 60:
            print("Grade is: Credit")
        
        
        
    
        
grade()             
              