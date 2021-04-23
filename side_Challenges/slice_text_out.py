'''
use slice to take out a certain segment of a long word.

word : "antidisestablishmentarianism"

slice and take the word "establishment' out of this long words 
and store it in a variable call answer"
'''

def extract(word, inword):
    prword = inword.casefold().strip()
    if prword == '':
        word ='antidisestablishmentarianism'
        prword='establishment'
        wbody = int(word.find(prword)) + int(len(prword))
        exword = word[ word.find(prword) : wbody ]
        obword = word[ :word.find(prword) ] + "_" + word[ wbody: ]
        print('extracting:', exword)
        print('from:',obword)
    elif prword.isalpha() == False:
        print('no numbers pls')
    else: 
        wbody = int(word.find(prword)) + int(len(prword))
        exword = word[word.find(prword):wbody]
        obword = word[:word.find(prword)] + "_" + word[wbody:]
        print('extracting:',exword)
        print('from:',obword)

if __name__=='__main__':
    word =input('enter text for filtering:',)
    inword = input('enter a word to extract:',)
    extract(word,inword)