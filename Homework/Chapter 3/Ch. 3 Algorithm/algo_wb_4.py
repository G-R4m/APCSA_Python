def grade():
    
    score = int(input("please input your grade as a percentage "))
    
    A_score = 89
    
    B_score = 79
    
    C_score = 69
    
    D_score = 59
    

    if score >= A_score:
        print('Your grade is A.')
    else:
        if score >= B_score:
            print('Your grade is B.')
        else:
            if score >= C_score:
                print('Your grade is C.')
            else:
                if score >= D_score:
                    print('Your grade is D.')
                else:
                    print('Your grade is F.')
                    
grade()