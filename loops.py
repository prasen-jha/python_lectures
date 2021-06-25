## While Loops

# a = 0 #loop intiator
# user = int(input('Enter a number: '))
# while a <= user:
#     print(a**2)
#     a += 1

data = 'Hello World!'

# i = 0
# while i <= len(data[0::3]):
#     print(data[i])
#     i += 1


# FOR Loops

# conditions for For loop:
#1. string
#2. range()
#3. iterable: Lists,Tuples,Dictionaries

# for i in data:
#     print(i)

# for _ in range(8):
#     user_input=input('enter value')

my_data = {'name':'dashkandhar','Tech':'Python','speciality':'Data Science'}

# for i,j in my_data.items():
#     print(i,'has value -->',j)

for i in my_data.values():
    if  i == 'dashkandhar':
        print(f'it\'s good to see you {i}')
        break
    else:
        print('Name not Found')
else:
    print('No data found')

# if is a statement which can be assumed 
# as a decider for the code block execution

flag = False

if flag:
    print('The flag is set to true')
else:
    print('the flag is fine')

# i = 0
# while i in range(10):
#     print(i**2)
#     i += 1
# else:
#     print('Loop exhausted')


a = 12
b = 3
result = 12//3

if result != 4:
    print('I will not work')
elif result >4:
    print('i will not work either')
elif result==4:
    print('Finally!My time')
else:
    print('Not at all')