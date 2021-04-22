'''
Ask the user for a number. Depending on whether the number 
is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?

Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) 
and one number to divide by (check). If check divides evenly into 
num, tell that to the user. If not, print a different 
appropriate message.
'''
oe = input('number:',)
oe = int(oe)
if oe >= 4:
    big = True
else:
    big = False

if oe % 4 == 0 and big == True:
    twon=input('enter 2 number',)
    num = int(twon[0])
    check = int(twon[1])
    if check % num == 0:
        print('clean')
    else:
        print('unclean')
elif oe % 2 == 0:
    print('even')
else :
    print('odd')
