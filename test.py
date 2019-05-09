# this code does nothing for the program, it sets up a a basic "Hello World" function.
def HW_Function():
    print("Hellow World!")
    print("Now I must go and learn more code")
#___________________________________________________

# setting up two global variables, name and nameInput, that will be use later in a section of code
name = " Daniel Carmichael"
# this code asks for a name input, "What is your name?:", down in the console. You will type your name in the console 
# and if that name is equal to the name var then the console will print Hello + your name or a name you choose.
nameInput = input("What is your name?: ")

# using an "if" statement to decide. if the code i want to compare is equal to one another
# I use a comparisson operand (==) to determine if the global variables are the same
if nameInput == name:

# using an "else" statement to run a block of code in the instance that the if statement returns false
    print("Hello" + name)
else:
    print('Goodbye')

    
    # the condensed code looks like this
def HW_Function():
print("Hellow World!")
print("Now I must go and learn more code")
#___________________________________________________

name = " Daniel Carmichael"
nameInput = input("What is your name?: ")
if nameInput == name:
    print("Hello" + name)
else:
    print('Goodbye')
# it is pretty simple, give it a try
