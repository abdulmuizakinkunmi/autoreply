print('This is a program for checking if a number is a binary or non binary')
while True:
    x=input('Enter the number you want to check: ')
    if '1' in x or '0' in x and '2' not in x and '3' not in x or '4' not in x or '5' not in x or '6' not in x or '7' not in x or '8' not in x or '9' not in x:
        print('This number is a binary number')
    elif '2' in x or '3' in x or '4' in x or '5' in x or '6' in x or '7' in x or '8' in x or '9' in x:
        print('This is not a binary number')
    else:
        print('Enter numbers only')


