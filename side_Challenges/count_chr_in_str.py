#2. Write a Python program to count repeated 
#characters in a string.



'''
word=input('entertext:', )
for char in word:
    charc = 0
    ccount = word.count(char)
    if ccount>1 and charc == 0 :
        charc = charc + 1
        print(char, ccount)
    else:
        break
'''

def crepchr(txt):
    cbox = dict()
    txt = txt.lower().replace(' ','').replace(',','').replace('.','').replace(';','').replace(':','')
    for x in txt:
        cbox[x] = cbox.get(x,0) + 1

        """ Old formula ~ simplified in to 'cbox[x] = cbox.get(x,0) + 1'
        if x not in txt:
            cbox[x] = 1
        else:
            cbox[x] = cbox[x] + 1 
        """
    if txt.isdigit == True:
        return 'I am unable to count numbers, please enter your text in alphabets.'
    else:
        print('This is the results:', sorted(cbox.items()))
        #for key,value in cbox.items():   #print out (key:value) in multiple lines.
        #    print (key,':',value)

if __name__=='__main__':
    txt=input('Enter Text to Count:', )
    crepchr(txt)
