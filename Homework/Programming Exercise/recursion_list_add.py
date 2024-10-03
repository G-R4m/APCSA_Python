def main():
    lst = []
    num_elements = int(input("How many elements do you want in the list? "))
    
    result = 0
    
    for i in range(num_elements):
        value = int(input(f"Enter element {i+1}: "))
        
        lst.append(value)
        
        result += sum(lst)
        
    print()
    print("The sum of your elements are:", result)
    
def sum(list):
    
    all_sums = 0
    
    if len(list) == 1:
        return list[0]
    
    else:
        all_sums += sum(list[1:]) #recursive step
        
    return all_sums
        
main()