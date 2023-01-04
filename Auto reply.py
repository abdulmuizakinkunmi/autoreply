import random
a=['Hi','Hello','Hey']
print('AUTO REPLY SOFTWARE')
while True:
    msg = input('Enter your message:').lower()
    if msg == 'hi'or msg =='hello'or msg =='hey':
        print(random.choice(a)+', '+ 'How are you?')
    elif msg == 'am fine':
        print('That is great')    
    elif msg == 'how are you'or msg == 'how far':
        print('Am fine')
    elif msg == 'good morning' or 'good afternoon' or 'good evening' :
        print('How have you been?')  
    else:
        print('Your message has been received, we will get back to you as soon as possible')        