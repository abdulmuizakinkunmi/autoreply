import math
b=int(input('Enter b:'))
a=int(input('Enter a:'))
c=int(input('Enter c:'))
def quadraticformula(b,a,c):
     print('x1=',-b+(math.sqrt(b*b-4*a*c)/2*a))
     print('x2=',-b-(math.sqrt(b*b-4*a*c)/2*a))
quadraticformula(b,a,c)     

 
