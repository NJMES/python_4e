'''
Ball Shift

Objective: 
the objective of this problem is to test the students' understadning on the doubly linked list.

Problem Description:
there are 'N' balls labelled with 1,2,3,...,N, from left to right. Now, we want to do two kinds of operations:

    1. "A x y ": move the ball labelled x to the left of the ball labelled y. where x!= y.
        reminder: if x is on the left of y, you may ignore this operation.
    2. "B x y": move the ball labelled x to the right of the ball labelled y, wherex!=y.
        reminder: if x is on the right of y, you may ignore this operation.
    3. 'R x': remove the ball labelled x.

print the final arrangemnt after M operations.

input:
the first line contains two integers, N(1<=N<=1000) and M(1<=M<=1000). 
the next M lines contain the operations.

output:
output the final arrangemnt of the 'N' balls from left to right. 
Each numbe is followed by a white space.

sample input:
10 5
A 2 1
A 10 1
A 5 6
B 6 9
R 3

sample output:
2 10 1 4 5 7 8 9 6

explanation:
operation 0: 1 2 3 4 5 6 7 8 9 10 
operation 1: 2 1 3 4 5 6 7 8 9 10
operation 2: 2 10 1 3 4 5 6 7 8 9
opeartion 3: 2 10 1 3 4 5 6 7 8 9
operation 4: 2 10 1 3 4 5 7 8 9 6
operation 5: 2 10 1 4 5 7 8 9 6

algorithm template:
1. what data structure should be used to simulate the operations?
2. what should be updated for insertion and deletion operation?
3. what is the complexity for your algorithm?
'''

#n = 10 , m = 5
n = input('The No. of balls:', )
m = input('The No. of operations:', )
ballbox = []

for i in range(0,int(n)):
    ballbox.append(i+1)

for o in range(0,int(m)):
    st = input('enter operations in format Operator/x/y:',  ).replace(',',' ').replace('/',' ').split()
    a = str(st[0]).lower()
    x = int(st[1])
    xpos=ballbox.index(x) 
    try :
        y = int(st[2])
        ypos=ballbox.index(y)   
    except:
        y = None  
        Print( 'I could not read the value of y' ) 

    if a == 'a':                
        if xpos > ypos:        # x > y = x on right of y. need to move x to the left y
            ballbox.insert(ypos, ballbox.pop(xpos)) #move an item that's already in the list to the specified position, you would have to delete it and insert it at the new position.
        else:
            print('A Ignore position change')

    elif a == 'b':
        if  xpos < ypos :     # y > x = x on the left of y. need to move x to the right of y
            ballbox.insert(ypos+1, ballbox.pop(xpos))
        else:
            print('B Ignore position change')

    elif a == 'r':
        ballbox.remove(int(x))
       
    else:
        print('nothing')

print(ballbox)      