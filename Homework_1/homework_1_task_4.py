import math

radius = input('Enter the radius in centimeters: ')

S = math.pi * float(radius) ** 2
S = round(S, 2)
print(f'The area of a circle is {S}')

