def property_tax():
    
    act_value = int(input("Please enter the actual value of your peice of property: "))
    
    asses_value = act_value * 0.60
    
    tax = asses_value / 100
        
    prop_tax = tax * 0.72
    
    print()
    print("The assessment value of your property is: $", asses_value)
    print("The tax for the property will be, $", format(prop_tax, ".2f"))
    
    
    
property_tax()