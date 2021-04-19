# 05iterationB.md

## Definite loops

    - quite often we have a list of items of the lines in a file - effectively a finite set of things.
    - we can write a loop to run the loop once for each of the items in a set of using the python for construct. 
    - these loops are called 'definite loops' because they execute an exact number of times.
    - we say that 'defnite loops iterate through the members of a set'
        #sample - simple definite loop
            for i in [5, 4, 3, 2, 1] : #i is going to be 5, then 4, ...
                print(i)
            print('blastoff')
        #Can be in Strings
            friends = ['jo', 'hi', 'sal'] 
            for friend in friends :
                print('happy new year:', friend)
            print('done')

## Simple definite loop

    - definite loops (for loops) have explicit iteration variables that changes each time through the loop. 
    - these iteration variables move through the sequence or set.

## Looking at "in"

    - the iteration variable "iteration" through the sequence (ordered set)
    - the block(body) of code is executed once for each value in the sequence
    - the iteration variable moves throught all of the value in the sequence.
      - sample - "in"
            for i in [5, 4, 3, 2, 1]: #i=iteration variable, []set;sequence
                print(i)

## 05 iterations B question

How many lines will the following code print?:

for i in [2,1,5]:
    print(i)

ans: 3
