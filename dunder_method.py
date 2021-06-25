'''

* The double Under score methods commonly known as dunder methods in Python
  are magic methods which by default is assigned to every python object or class
  you create.

* You can override these methods according to your need.

'''


## this function is given it a triple quoted string which will automatically
## be converted into the documentation of this code that's why they are called
#  "MAGIC METHODS"




def welcome():
    '''
    it's just a basic function which prints hello world for no reason
    ''' 
    print('HelloWorld')




# calling all the methods given by python in the backend
print(dir(welcome))

#calling dunder doc for seeing the documentation of code
print(welcome.__doc__)

#all the global variables for this method
print(welcome.__globals__)

