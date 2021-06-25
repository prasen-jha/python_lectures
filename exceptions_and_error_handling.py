import requests # a library to process https/http requests
import logging

'''
Errors or mistakes in a program are often referred to as bugs.
They are almost always the fault of the programmer.
The process of finding and eliminating errors is called debugging.
Errors can be classified into three major groups:

    Syntax errors
    Runtime errors
    Logical errors

Python syntax errors include:

    leaving out a keyword
    putting a keyword in the wrong place
    leaving out a symbol, such as a colon, comma or brackets
    misspelling a keyword
    incorrect indentation
    empty block

    def myfun():
        pass

Some examples of Python runtime errors:

    division by zero
    performing an operation on incompatible types
    using an identifier which has not been defined
    accessing a list element, dictionary value or object attribute which doesn’t exist
    trying to access a file which doesn’t exist

some examples of mistakes which lead to logical errors:

    using the wrong variable name
    indenting a block to the wrong level
    using integer division instead of floating-point division
    getting operator precedence wrong
    making a mistake in a boolean expression
    off-by-one, and other numerical errors

'''




## just creating a file 
try:
    with open('dummy_file.txt','w+') as f:
        f.write('dummy contents of a stupid file!')
except Exception as e:
    print(e)

try:
    with open('dummy_file.txt','w+') as f:
        f.write('dummy contents of a stupid file!')
except Exception as e:
    print(e)

# log messages to a file, ignoring anything less severe than ERROR
logging.basicConfig(filename='myprogram.log', level=logging.ERROR)

# these messages should appear in our file
logging.error("The washing machine is leaking!")
logging.critical("The house is on fire!")

# but these ones won't
logging.warning("We're almost out of milk.")
logging.info("It's sunny today.")
logging.debug("I had eggs for breakfast.")


try:
    age = int(input("How old are you? "))
except ValueError as err:
    logging.exception(err)



'''

    Write logging configuration for a program which logs to a file called log.txt and discards all logs less important than INFO.
    Rewrite the second program from exercise 2 so that it uses this logging configuration instead of printing messages to the console (except for the first print statement, which is the purpose of the function).
    Do the same with the third program from exercise 2.

'''

