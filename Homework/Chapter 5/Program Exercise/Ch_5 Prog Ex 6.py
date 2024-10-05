def calorie_calc():
    
    grams_fat = int(input("Please enter the number of fat grams you consumed today: "))
    
    calories_from_fat = grams_fat * 9
    
    print()
    print("The calories from fat that you are recieving is:",  calories_from_fat)
    print()
    
    grams_carb = int(input("Now please enter the number of carb grams you consumed today: "))
    
    calories_from_carb = grams_carb * 4
    
    print()
    print("The calories from carbohydrates that you are recieving is:", calories_from_carb)
    
    
calorie_calc()