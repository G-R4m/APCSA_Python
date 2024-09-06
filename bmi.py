# A program that asks the user for their height and
# weight in inches and pounds, respectively.
# Calculate BMI

def bmi():
    
    a = 1
    
    while a > 0: 
    
        print('This program will compute BMI')
        
        height = float(input('Please enter your hering in meters: '))
        mass = float(input('Please enter your weight in kilograms: '))
        
        #compute adn display BMI.
        
        bmi = (mass/height **2)
        
        bmi = int(bmi *10)/10 ##keeps result as a real nuber with one decimal place
        
        print('Current BMI with a weight of ', mass, ' and a height of ', height, 'is', bmi)
        
        if bmi >= 30.0:
            print ("Obese")
            
        if bmi >= 25.0 and bmi <= 29.9:
            print("Overweigth")
            
        if bmi >= 18.5 and bmi <= 24.9:
            print ("Healthy")
            
        if bmi < 18.5:
            print ("Underweight")
            
        a= int(input("Continue? Press 0 for NO, and 1 for YES  "))
    
bmi()