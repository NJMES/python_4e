
'''
##building our own functions.
-   we created a new function using the def keyword followed by optional parameters in parentheses.
-   we indent the body of the function.
-   this defined the function buut does not execute the body ot the function.
        ##sample
        def newfunction():
            print('i am being defined, i wont be printed.')
        ##

#Define and uses.
-   once we have defined a function, we can call(or invoke) it as many times as we like.
-   this is the store and reuse pattern.

##arguments
-   argument is a vlaue we pass into the function as its input when we call the funtion.
-   we use arguments so we can direct the cuntion to do different kinds of work when we call it at differnt times.
-   we put the arguments in parentheses after the name of the function.
        ##sample
        big = max('Hello world') #hello world is the argument. #max is the function.
        ##

#Parameters.
-   a parameter is a variable which we use in the function definition. 
    -   it is a 'handle' that allows the code in the function to access the arguments for a particular function invocation.
            ##sample
            def greet(lang):    #lang is a parameter
                if lang == 'es':
                    print ('hola')
                elseif lang == 'fr':
                    print (Bonjour')
                else
                    print ('hello')
            greet('en')
            #result hello
            ##

##return values.
-   often a fucntion will take its arguments, do some computation, and return a value to be used as the
     value of the fucntion call in the calling expression. the return keyword is used for this.
        ##sample
        def greet():
            return 'Hello'
        print(greet(), 'Glenn')
        #result Hello Glenn
        ##
-   a fruitful function is one that produces a result (or return value)
-   the return statement ends the function execution and 'sends back' the result of the function.

##multiple parameters / arguments.
-   we can define more than one parameter in the function definiiton.
-   we simply add more arguments when we call the function.
-   we match the number and order of arguments and parameters.
        ##sample
        def addtwo(a, b):
            added = a + b
            return added
        x = addtwo(3, 5)
        print(x)
        #result 8
        ##

##Void (non-fruitful) functions
-   when a function does not return a value , we call it a void function.
-   void function are not fruitful.

##to function or not to function...

##04 function B question.
What will the following Python program print out?:

def fred():
    print("Zap")
def jane():
    print("ABC")

jane()
fred()
jane()

#ans : 
ABC
Zap
ABC


'''