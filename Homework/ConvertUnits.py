#File: ConvertUnits.py
#Student: Giancarlo Ramirez
#
#Date: September 17, 2024
#This program will take any input of inches and feet (as long as it's not negative) and will convert it to both English units and Metric Units
#Github: G-R4m





def conversion():
    print("Hello user! I will convert your feet and inches to litteraly everything!")
    print()
    
    input_f = float(input("Please enter any number of feet: "))
    input_in = float(input("Please enter any number of inch: "))
    
    inch = (input_f * 12) + input_in
    
    feet = inch / 12
    
    yard = feet / 3
    
    miles = feet / 5280
    
    meters = feet * 0.3048
    
    cent = meters * 100
    
    milli = cent + 10
    
    kilo = meters / 1000
    
    print("You've chosen:", input_f, "feet and", input_in, "inches")
    print()
    print("This converts to....")
    print()
    print()
    
    print("Superior American System (English Units):")
    print("     Feet:", feet)
    print("     Inches:", inch)
    print("     Yards:", yard)
    print("     Miles:", miles)
    
    print()
    print()
    
    print("Stinky Other System (Metric Units):")
    print("     Meters:", meters)
    print("     Centimeters:", cent)
    print("     Millimeters:", milli)
    print("     Kilometers:", kilo)
    
    
    
conversion()