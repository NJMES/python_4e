#Write a programs that can convert number 1 to 7 in integer 
# or text into day of the week?

day=input('day:', )

lday= day.lower() 
if lday == 'one': #how to compare other permutations. One/ONE/oNe use day.lower() to make it all lower case.
    day=1
elif lday == 'two':
    day=2
elif lday == 'three':
    day=3
elif lday == 'four':
    day=4
elif lday =='five':
    day=5
elif lday =='six':
    day=6
elif lday =='seven':
    day=7
else:
    print('not something i understand')
    day=0

nday=int(day)

try:
    if nday == 1:
        print('monday')
    elif nday == 2:
        print('tuesday')
    elif nday == 3:
        print('wednesday')
    elif nday == 4:
        print('thursday')
    elif nday == 5:
        print('friday')
    elif nday == 6:
        print('saturday')
    elif nday == 7:
        print('sunday')
    else:
        print('i only understand 1 to 7 in text or numbers')
except:
    print('not something i understand')
