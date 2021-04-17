# 05 iterations A

link: <https://youtu.be/dLA-szNRnUY>

## loops and iterations.  [[loops]]

## repeated steps

    - loop(repeated steps) have iteration variables that change each time throught a loop. 
    - often these iteration variables go through a sequence of nunmbers.
    - While ~ creates a condition and iteration variable.
    sample - loop with iteration variables.
        n = 5
        while n > 0 :   #variable 
            print(n)
            n = n - 1   #iteration.
        print('blastoff')
        print n 
    #while checks for condition n > 0. #if n == 0, fufill condition and go to print('blastoff') & print n

    sample - infinite loop.
        n = 5
        while n > 0:   #Variable is not iterated. Goes into infinite loop.
            print('A') #no iteration.
        print('Finish') #can't be run, cause n = 5 ; While can't be completed. 
    # while will keep checking the condition till it is fufilled, and run the next operation.
    # if n=0, 'While' will check that is False and skip right to print('blastoff') & print n.

## Break out of a loop

    - the break statement ends the current loop and jumps to the statement immediately following the loop.
    - it is like a loop test that can happend anywhere in the boday of the loop.
    #sample - breaking out of a loop.
        while True:
            line = input('> ')  #produce an input field '> '
            if line == 'done' #if input done == done
                break         #trigger breakout into the outer statement.
            print line #will just keep requesting input till matches 'done'
        print('Done!')
    #break will exits into the outer next line #breakout of the loop.

## Finishing an iteration with Continue
    
    - continue statement ends the current iteratio and jumps to the topo of the loop and states the nest itereation.
    #sample - iteration with continue.
        while True:             #check for 'True condition',
            line = input('> ')  #input field '> ...'
            if line[0] == "#" : #if line 0 contain '#'
                continue        #restart and run the start loop again.
            if line == 'done':  #if line contain done
                break           #break out of loop and run next line.
            print(line)
        print('Done')

## indefinite loops

    - while loops are called "indefinite loops" becaus they keep going until a logical condition becomes 'False'.
    - the loops we have seen so far are pretty easy to examine to see if they will terminate or if tey will be "indefinite loops"
    - sometimes it is a little harder to be sure if a loop will terminate.

## 05 question iteration A

What will the following code print out?:
n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1

ans:
0
1
2 #breaks out on 3 #3 is not printed.
