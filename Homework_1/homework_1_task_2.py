text = input('What is your favorite book: ')
number = len(text)

if number == 0:
    print('Please answer the question.')
elif number <= 20:
    print('Thank you for your answer!')
else:
    print(f'Ups:) Your answer contains {number} symbols. You can use up to 20 symbols.')
