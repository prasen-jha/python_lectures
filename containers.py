import os,random


'''
we forgot to cover the following concepts in containers which are as following

1. Sets
2. range() 

'''

#Sets:A set is a collection of unique elements. If we add multiple copies of 
# the same element to a set, the duplicates will be eliminated,
#  #and we will be left with one of each element

list_data_with_same_elements = [1,2,3,1,4,1,5,6,4,5,8,11,14,12,11,56,56]

collection_of_unique_elements = set(list_data_with_same_elements)
print(collection_of_unique_elements)

#thing to consider here is that a dictionary and set in python has same representation so,
# writing my_data = {}, --> will create dictionary not a set
# to instaniate a set we write my_data = set(iterable).

#SET OPERATIONS:set supports all those operation which we have read in mathematics
# i.e Intersection, Symettric difference,Union and i forgot few others

a = {random.randint(1,20) for i in range(20)}
print(type(a))

b = {random.randint(1,20) for i in range(20)}

print(a,b,end='\n')

#operations
#1. symmetric difference
c = a-b
print(c)

#2.Union
d = a|b
print(d)

#3.Intersection
e = a&b #what it is doing
print(e)

#4.or differnce
f = a^b
print(f)

####It is important to note that unlike lists and tuples sets are not ordered. 
# When we print a set, the order of the elements will be random. 
# If we want to process the contents of a set in a particular order, 
# we will first need to convert it to a list or tuple and sort it

##-------------------------------------------------------<------>------------------------------------------------------------------##

##RANGE

##range is another kind of immutable sequence type(list). 
# It is very specialised – we use it to create ranges of integers. 
# Ranges are generators. Which We will find out more about generators in coming lectures, 
# but for now we just need to know that the numbers in the range are generated one at a time as they are needed, 
# and not all at once


## CHALLENGE FOR CLASS LEARNING

'''

    Convert a list which contains the numbers 1, 1, 2, 3 and 3, and convert it to a tuple a.
    Convert a to a list b. Print its length.
    Convert b to a set c. Print its length.
    Convert c to a list d. Print its length.
    Create a range which starts at 1 and ends at 10. Convert it to a list e.
    Create the directory dict from the previous example. Create a list t which contains all the key-value pairs from the dictionary as tuples.
    Create a list v of all the values in the dictionary.
    Create a list k of all the keys in he dictionary.
    Create a string s which contains the word "antidisestablishmentarianism". Use the sorted function on it. What is the output type? Concatenate the letters in the output to a string s2.
    Split the string "the quick brown fox jumped over the lazy dog" into a list w of individual words.

'''


