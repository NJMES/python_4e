#2. Write a Python program to count repeated 
#characters in a string.

word=input('entertext:', )
char='abcdefghijklmnopqrstuv'

for char in word:
    ccount = word.count(char)
    if ccount>1 :
        print(char, ccount)