#File: ComputeTaxes.py
#Giancarlo Ramirez
#
#September 25, 2024
#This program is made to compute taxes on any ammount depending on whether the user's marital status
#GitHub: G-R4m

def tax():
    print("Welcome! Your taxes will be sorted out soon! Just a quick question about your marital status:")
    print()
    status = input("  Please input 's' if single, and 'm' if married: ")
    
    
    if status == "s":
        income = float(input("  Please enter your taxable income: "))
        print()
        
        if income < 0:
            print("Negative income reported! Try again later....")
            
        elif income < 8000 and income >= 0:
            tax = income * 0.10
            
        elif income < 32000 and income >= 8000:
            tax = 800 + (income - 8000) * 0.15
            
        else:
            tax = 4400 + (income - 32000) * 0.25
            
        print("Marital status: Single")
        print("Taxable income: $", format(income, ".2f")) #in order to round the number to 2 decimal places
        print("Taxes owed: $", format(tax, ".2f")) #in order to round the number to 2 decimal places
            
        
    elif status == "m":
        income = float(input("Please enter your taxable income: "))
        print()
        
        if income < 0:
            print("Negative income reported! Try again later....")
            
        elif income < 16000 and income >= 0:
            tax = income * 0.10
            
        elif income < 64000 and income >= 16000:
            tax = 1600 + (income - 16000) * 0.15
            
        else:
            tax = 8800 + (income - 64000) * 0.25
            
        print("Marital status: Married")
        print("Taxable income: $", format(income, ".2f")) #in order to round the number to 2 decimal places
        print("Taxes owed: $", format(tax, ".2f")) #in order to round the number to 2 decimal places
        
        if income < 0:
            print("Negative income reported! Try again later....")
    
    else:
        print("Entered an invalid response :( Try again later!")
    
    
    
tax()
