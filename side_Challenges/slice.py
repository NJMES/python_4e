'''
use slice to take out a certain segment of a long word.

word : "antidisestablishmentarianism"

slice and take the word "establishment' out of this long words 
and store it in a variable call answer"
'''

word ='antidisestablishmentarianism'
inword = input('enter a word to extract:',)
prword = inword.casefold().strip()
if prword == '':
    fword='establishment'
    spt= word.find(fword)
    ept= len(fword)
    wbody = int(spt)+int(ept)
    exword = word[spt:wbody]
    obword = word[:spt] + "" + word[wbody:]
    print('extracting:', exword)
    print('from:',obword)
elif prword.isalpha() == False:
    print('no numbers pls')
else: 
    spt= word.find(prword)
    ept= len(prword)
    wbody = int(spt)+int(ept)
    exword = word[spt:wbody]
    obword = word[:spt] + " " + word[wbody:]
    print('extracting:',exword)
    print('from:',obword)
