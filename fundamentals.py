# Mixing in some user defined functions
# This is slightly more advanced but done worry if you do not understand them yet
# It's still good to familiarise your self with them even if you dont understand them yet.

#1 | Indexing in a variable, in a funnction

def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

row_1 = ['', '', '']
row_2 = ['', '', '']
row_3 = ['', '', '']



row_2[1] = 'x'

display(row_1, row_2, row_3)

#3 | LEGB

#A standard process that exists for python is known as LEGB.

#I wanted to bring this up just so you know it exists seeing how I just learned about it last
#night.

# L
#  This stands for local. Local is a term used for variables/names used in a function.
#  If they are defined in that function for example X = 20, but outside of the function
#  it is defined as x = 30, Python will use the x = 20 rather than x = 30 unless defined as global.

# E
# E stands for enclosing locals. I will provide an example below to give more context.
# Enclosing locals means names in local scope of any and all enclosing functions from inner to outer.

# G
# G stands for global. Global means names assigned at the top of a module file.
# Or declared global in a definition.

# B stands for builtin. Builtin would be anything from print, type, list, to other pre-defined names.

# You can always tell if something is pre-defined by the syntax highliting or if you can use the 'help' function on it.

example
# below is global
name = 'this is a global string'


# we grab sammy first because that is the local name
# if sammy was not there we would grab the global variable for name if present
# in this case it is so we would grab our first instance of the variable name
# global is also defined by having no indentation

# below is enclosing <<<<<<<<<<<<<<
def greet():
    name = sammy

    def hello():
        # below is local <<<<<<<<<<<<
        name = 'i am local'
        print('hello ' + name)

    hello()


greet()

# This is a decent amount to chew on, so I will leave it at this for today's entry in to warmups.
