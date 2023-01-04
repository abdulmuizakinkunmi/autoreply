print('This is a contact book to save contacts')
a=[]
while True:
    instruction=input('''
            Press A if you want to add your name to contacts
            Press B if you want to check saved contacts
=''')
    if instruction == 'a':
        x = input('Enter your name and number in this format Ade:09011112222= ')
        a.append(x)
        print('Your name and phone number has been registered')
    elif instruction == 'b':
        for x in a:
            print(x)







