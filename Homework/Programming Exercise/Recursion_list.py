def main():
    lst = []
    num_elements = int(input("How many elements do you want in the list? "))
    
    for i in range(num_elements):
        value = int(input(f"Enter element {i+1}: "))
        lst.append(value)
        
    largest_value = bigg(lst)
    print(largest_value)
    
def bigg(list):
    if len(list) == 1:
        return list[0]
        
    else:
        largest = bigg(list[1:]) #recursive step
        if list[0] > largest:
            return list[0]
        else:
            return largest
        
main()