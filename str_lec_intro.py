'''
1.Everything in python comes from a class that means the data has been already 
predifined and will be decided on the basis some special characters and 
as it is a class it has various built in functions.

2.
a.) In Python colons ':' are used in following cases:

            if some condition:
                pass
            elif some other condition:
                do something else:
            else:
                the last statement which will be executed in the end if nothing works

        simimlarly we can use it with statements like while,for,try,except,finally
        these are called statements and are used for making logical decisions on boolean result

b.) when creating a function or class such as

    def myfunc():
        print('hello world!)


    class MyClass:
        pass


    !!!Python does let you use a semi-colon to denote the end of a 
    statement if you are including more than one statement on a line.
    if value1; if valu2



3.Python has some reserved functions 
which is very commonly used bydevelopers such as 
print():'My personal favourite the most beautiful
debugging tool',range(),zip(),list(),str(),int(),map(),reduce() and lot other cool ones!



4.Python has a growing community that's why we have a lot of third 
party softwares at our disposal which we can install
from Python pip(Python Package Index),PIP is a package manager for Python packages) 
for installing we write 
            python -m pip install package_name



5. We import the package while developing code by writing 
        import my_package; this statement loads all the functions in the module called 
        and is used as 
            my_package.my_func()

but to be more descriptive you can call the particular function as 
        from my_package import myfunc 

and you can create short alias as 
        import mylibrary as mb
        mb.func()

### do pay attention various other things that will be taught while coding on the screen so let's get started...

6. Python supports explicit conversion in between objects
 in general sense an int-->str, str-->list and so on 

'''






# strings are identified by single quotes, double_quotes  and triple quotes
'string_data'  #this is a string


string_variable = 'dashkandhar' # here string_variable is the name of pointer on memory 
                                #which is holding the data 'dashkanhar',
                                # and '=' is knowm as assignment operator



# the function that are most widely used  with any object in python are 
print('Hello world!') #the most common function that is print, which echoes the value or argument passed on the output screen
#Hello world!

print(type(string_variable)) # returns class to which the data stored in variable belongs to.
#<class 'str'>

print(dir(string_variable)) # returns a list or fondly known as directory of methods available on that class
'''['__add__', '__class__', '__contains__', '__delattr__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
 '__getitem__', '__getnewargs__', '__gt__', '__hash__', 
 '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']'''


# we can access functions to do basic operations for e.g:

print(string_variable.upper()) # returns a uppercase value 
print(string_variable.endswith('r')) # returns True/False on the basis of the value passed for checking.

another_var = 'Hello world! It\'s Python'
print(another_var.split()) # returns a list of substrings seperated by empty spaces
print(another_var.find('world')) #returns the index at which the substring is found

## try other functions yourself...........


## Strings support indexing and slicing operations on them
data = 'dashkandhar'

print(data[4]) # gives value at 3rd index

print(data[1:6]) #gives value from 1st position to 5th position

b = data[0::]

print(b) #will give values from starting to end and is used while creating duplicate data keeping the original one

print(data[-1]) # negative indexing to get data from the end 



## STRINGS ARE IMMUTABLE IN PYTHON i.e you cannot directly mutate but with explicit conversion we can acheive mutation for e.g
new_data = list(data)
new_data[4] = 'z'
print(''.join(new_data))

## boolean checking on strings with in statement
print('hello' in another_var.lower())

## condition with logic of concatenation
if 'hello' in another_var.lower():
    print(f'{another_var}'+'it\'s python') # string formatter is used



## looping through a string
for i in another_var:  
    #i is the iterator which will 
    #rotate through each element in the variable,
    # this iteration functionality comes from __iter__
    print(i,end='\n')

## concatenation : two strings can be added this is achieved through __add__
a = 'Gotta Do'
b = 'That what is needed to !'
print(a+' '+b)

## multplication is also possible and that is done with the help __mul__ method but it is supported between a string and an integer
a = 'Hello'
print(a*3)

# 'a'*'b'
# # ## on the other hand multiplying two strings will generate TypeError

user_input = input('Enter a string and i will show you all python functions for it: ')

print(user_input.capitalize())
print(user_input.center(len(user_input),'@'))
print(user_input.isupper())
print(user_input.split())
print(user_input.join(['Hello !']))









