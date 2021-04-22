#2. Write a Python program to count repeated 
#characters in a string.

word=input('entertext:', )

for char in word:
    ccount = word.count(char)
    charc = 0
    if ccount>1 and charc == 0 :
        print(char, ccount)
        charc = charc + 1
    