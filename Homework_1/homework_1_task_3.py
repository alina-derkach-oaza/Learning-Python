a = input('Enter the length of the first side of a triangle: ')
b = input('Enter the length of the second side of a triangle: ')
c = input('Enter the length of the third  side of a triangle: ')

a = int(a)
b = int(b)
c = int(c)

if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        print('Triangle exists!')
    else:
        print('Triangle does not exist!')
else:
    print('All sides must be greater than 0')
