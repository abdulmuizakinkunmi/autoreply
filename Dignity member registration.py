print('**************DIGNITY MEMBERS REGISTRATION******************')
a=[]
while True:
     instruction=input('''
                                INSTRUCTION:
                                1. Enter R if you want to register: 
                                2. Enter C if you want to check registered members: 
                                3. Enter Q if you want to quit:''')
     if instruction=='r':
         name=input('Enter your name: ')
         a.append(name)
         print('Dear',name,'YOU HAVE BEEN SUCCESSFULLY REGISTERED TO DIGNITY ACADEMY')
     elif instruction=='c':
         print(a)
         print('THANKS FOR CHECKING OUR MEMBERS\nYOU CAN ALSO REGISTER WITH OUR ACADEMY')
     elif instruction=='q':
         quit()
     else:
         print('Enter the correct instruction')
   
         
         
        
    
                               

   
   
    
