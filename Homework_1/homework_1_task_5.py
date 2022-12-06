shopping_list = {}

cont = 'Y'
while cont == 'Y':
    product = input('Enter the product name: ')
    price = input('Enter the product price: ')
    shopping_list.update({product: price})
    cont = input('Do you want to continue? (Y/N): ')

print('Your shopping list: ')
print(shopping_list)
