Name=input('ENTER YOUR NAME:').upper()
Score=int(input('ENTER YOUR SCORE:'))
if Score>= 80 and Score<= 100:
    print('Hello',Name,'you have Grade A')
    print('Remark: An excellent result. keep it up !')
elif Score>= 70 and Score<80:
    print('Hello',Name,'you have Grade B')
    print('Remark: A very good result. keep it up !')
elif Score>= 60 and Score<70:
    print('Hello',Name,'you have Grade C')
    print('Remark: A good result. keep it up !')
elif Score>= 50 and Score<60:
    print('Hello',Name,'you have Grade D')
    print('Remark: A weak result. work harder next time !')
elif Score>= 40 and Score<50:
    print('Hello',Name,'you have Grade E')
    print('Remark: A very weak result.work harder next time !')
elif Score<40:
    print('Hello',Name,'you have Grade F')
    print('Remark: Fail. To repeat !')
else:
    print('WRONG INPUT !!!')
