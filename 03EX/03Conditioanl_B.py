#03Conditioanl_B

#multi-way branch.
""" example | multi-way branch 1 our to 3.
x = ?
if x < 2 :
    print('small')
elseif x < 10 :
    print('medium')
else :
    print('LARGE')
print('all done')
"""
#*else* is the catch all. if 'else' is not us to end the branch *print result* might have been skipped.
#you can start with 'IF" multiple 'elseif' and end the branch with 'else'

"""
try/except structure.
-   you surround a dangerous section of code with try and except.
-   if the code in the try works - the except is skipped.
-   if the code in the try fails - jumps to the except section.
"""

''' try/except example - run dangerous code. 
astr = 'bob'
try :
    istr = int (astr)
except : 
    istr = -1
print('first:', istr) 
#result first: -1

astr = "123"
try :
    istr = int (astr)
except : 
    istr = -1
print('second:', istr) 
#result second: 123
'''

''' try/exept sample
rawstr = input('enter a number:')
try : 
    ival = int(rawstr)
except:
    ival = -1

if ival > 0 :
    print('nice work')
else : 
    print('not a number')

#result nice work if you if you enter integer 42 
#result not a number if your enter string 'forty-two'
'''

'''summary of 03 Conditinoal structures.
== <= >= > < != =
indentation : 
one-way decisions
two-way decisions
nested decisions.
multiway decisions. using elseif.
try/except to compensate for errors.
'''
