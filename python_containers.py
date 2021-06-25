# # #1. Lists: are the containers in which we can store heterofenous data and which can be modified\
# # ##  later on as per demand
# # #2. Lists are mutable as seen in the examples of string


# list_data = ['dashkandhar',[1,2,3,4,5],'Python','C','C++']

# # # indexing
# # print(list_data[1][0:4])

# # #slicing
# # print(list_data[0::])

# # #reverse ordering
# # print(list_data[-4])

# # ## adding elements to a list
# # list_data.append('Java')
# # print(list_data)

# # Creating a copy
# b = list_data.copy()
# print(b)

# print(id(list_data) == id(b))


# # #clearing the copy
# # print(b.clear())
# # print(b)

# # #count an element from the data
# # print(list_data.count('Python'))

# # # extending a list
# # c = ['students','learning']
# # list_data.extend(c)
# # print(list_data)

# # #finding the index
# # print(list_data.index('students'))

# # #inserting
# # list_data.insert(5,'Tina')
# # print(list_data)


# # # removing element from the last
# # print(list_data.pop())

# # # rtemoving particular element
# # list_data.remove('students')
# # print(list_data)

# # # reversing the list
# # list_data.reverse()
# # print(list_data)

# # # sorting the lis * sorting works on homogenous data
# # data = [10,20,25,2,4,8]
# # data.sort()
# # print(data)

# # 2. TUPLES: data container which cannot be modified once created 

# tuple_data = (1,2,3,4,5,6)
# print(type(tuple_data))

# # tuple_data[0] = 'str'

# print(list(tuple_data))

# #3. Dictionaries

# dict_data = {'Name':'Dashkandhar','Tech':['Python','Data Science'],'Hobby':'Adventures'}

# print(dict_data['Tech'])
# print(dict_data.get('Name'))

# for k,v in dict_data.items():
#     print(f'key {k} has value {v} which is data of type {type(v)}')


# comprehension = [x**2 for x in range(100) if x%2==0]
# print(comprehension)

# comp = []
# for x in range(100):
#     if x%2==0:
#         comp.append(x**2)
# print(comp)


# dict_comp = {x:x**2 for x in range(100) if x%2==0}
# print(dict_comp)

list1 = range(20)

list2 = range(20,30)

list3 = list(zip(list1,list2))

print(list3)