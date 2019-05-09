# this code does nothing for the program, it sets up a a basic "Hello World" function.
def HW_Function():
    print("Hellow World!")
    print("Now I must go and learn more code")
#___________________________________________________

# setting up two global variables, name and nameInput, that will be use later in a section of code
name = " Daniel Carmichael"
nameInput = " Daniel Carmichael"

# using an "if" statement to decide. if the code i want to equate is equal to one another
# I use a comparisson operator (==) to determine if the global variables are the same
if nameInput == name:

# using an "else" statement to run a block of code in the instance that the if statement returns false
    print("Hello" + name)
else:
    print('Goodbye')
