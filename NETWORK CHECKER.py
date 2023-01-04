a=int(input('Enter phone number:'))
new_a=str(a)
arr=new_a[0:2]
provider=new_a[2]
if arr=='80' or arr=='81' or arr=='90' or arr=='91' or arr=='70':
    if provider=='3' or provider=='6' or  provider=='0' or provider=='4':
        print('The phone number is a MTN number')
    elif provider=='1' or provider=='5' or  provider=='7':
        print('The phone number is a GLO number')
    elif provider=='8' or provider=='2':
        print('The phone number is an AIRTEL number')
    elif provider=='0' or provider=='8' or  provider=='9':
        print('The phone number is an ETISALAT number')
else:
    print('WRONG INPUT')
        
