def main():
    x = 1
    y = 3.4
    print(x, y) #will print 1, 3.5
    change_us(x, y) #will not print 0, 0 since x and y are changed ONLY in that function
    print(x, y) #will print 1, 3.4 once more

def change_us(a, b):
    a = 0
    b = 0
    print(a, b)

main()