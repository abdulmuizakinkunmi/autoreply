print('THIS IS A SECRET NOTE FOR YOUR PRIVACY')
a=[]
b=[]
while True:
    instruction = input('''
                 INSTRUCTIONS:
                 press 1 if you want to add a note.
                 press 2 if you want to check your note.
    =''')
    if instruction == '1':
        c = input("Enter your note's content: ")
        d = input('Form a password: ')
        a.append(c)
        b.append(d)
        print('YOUR NOTE IS SUCCESSFULLY ADDED !!!')
    elif instruction == '2':
        e = input('Enter your password: ')
        if e in b:
            print(a)
        else:
            print('ENTER THE CORRECT PASSWORD !!!')
    else:
        print('CHECK THE INSTRUCTIONS AND ENTER THE CORRECT INSTRUCTION')
