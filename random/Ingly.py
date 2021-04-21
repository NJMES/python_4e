'''
Example of exercises I thought were interesting to try:
1. Write a Python program to add 'ing' at the end of a given string 
(length should be at least 3). If the given string already 
ends with 'ing' then add 'ly' instead. If the string length 
of the given string is less than 3, leave it unchanged.
'''

word=input('enter text:', )
wl=len(word)
ingc= word.endswith('ing')  #ingc= 'ing' in word

if wl >= 3 and ingc == False:
    ingw = word + 'ing'
    print(ingw)
    
elif wl >= 3 and ingc == True:
    ly= word.replace('ing','ly')
    print(ly)
    
else:
    print(word)
    