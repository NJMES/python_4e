'''
Define a function that takes in two inputs

The first input will be a string that contains multiple occurrences of a word.

The word may be broken up into smaller parts and separated by one or more characters 
within the string.

The word may contain upper and lower case characters and may also be split up 
by some special characters.

The 5 special characters are: . , _ - {SPACE}
({SPACE} means an empty space and not literally the word)

For example, if the word is "apple", the following strings below are considered as 
valid occurrences:
apple
AppLe
a,p.p-l _e

The second input will be the word that can be found within the string.

The final output should be the number of occurrences of the word.

Example Test Case:
1st Input: a s-j.sba nanananaok_-.kSjaB a nan a_n.A-n_sKe-Kd.ab.A-n A .-n.adsba_-.Na-_nAo.feas.f-_fas
2nd Input: Banana
Output: 4
'''

def count(tsent, fword):
    tsent = tsent.lower().replace('.','').replace('_', '').replace('-','').replace(',','').replace(' ','')
    o = tsent.count(fword.lower())
    return o

def count2(tsent, fword):
    tsent = tsent.lower()
    spchar = '.,_- '
    trim=''
    for i in tsent:                     #run through tsent-string in sequence.
        if i not in spchar:             #check if i not in special char, if its not in special char run below.
            trim = trim + i             #trim get asign with existing trim string + new filtered i string.
    print(trim)
    o = trim.count(fword.lower())
    return o


if __name__=='__main__':
    tsent = input('Ent3r y0uR W3irD +3Xt H3re:', )
    fword = input('What is the word you are looking for:', )
    output = count( tsent, fword)
    #output = count2(tsent,fword)       #another way to filter.
    print(' *',fword,'*  appeared  *',output,'*  times in your entry.')
    