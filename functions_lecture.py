import requests
import sys,os
import smtplib
# pip install SpeechRecognition
# pip install pyaudio

# # # def hello(name):
# # #     try:
# # #         if isinstance(name,str):
# # #             print(f'hello {name} it\'s a pleasure')
# # #     except Exception as e:
# # #         print(e)
# # # hello('prasenjit')

# # # a = hello
# # # print(a)


# # var = 'This is a string'
# # temp = var.split()
# # print(temp[1])
# # temp[1] = 'was'
# # new_var = ' '.join(temp)
# # print(new_var)

# def mutate_string(string,value,index):
    
#     '''
#     this function takes in one string and makes a list out of it 
#     and according to the index ofgiven it will replace the value of string.
#     index should be assigned to the values but not the spaces.
#     '''
#     temp = list(string)
#     temp[index] = value
#     new_var = ' '.join(temp)
#     return new_var



# # print(mutate_string.__doc__)

# # var = input('Enter the string: ')
# # quantity = input('Enter the value you want: ')
# # index = int(input('Enter the position you want to update: '))
# # b = mutate_string(var,quantity,index)
# # print(b)

# def greeting_name(title,name,surname,formal =True,time=None):

#     if formal:
#         fullname = f'{title} {surname}'
#     else:
#         fullname = f'{name}'
    
#     if time is None:
#         greeting = 'Hello'
#     else:
#         greeting = 'Good %s' %time
#     return '%s %s' %(greeting,fullname)


# a =greeting_name('Mr.','Prtasenjit','Jha')
# print(a)
# b =greeting_name('Miss','Harmandeep','Kaur',formal=False,time='Morning')
# print(b)
# c = greeting_name('Mr','Anurag','Verma',formal =True)
# print(c)

# def palindrome_checker(string):
#     # to do: you have to return the result i9n True or False
#     try:
#         if isinstance(string,str):
#             if string.lower()[0::] == string.lower()[::-1]:
#                 print('Palindrome Found')
#             else:
#                 print('It\'s not a palindrome')
#         else:
#             raise Exception('Data is not string')
#     except ValueError as e:
#         print(e)



# def scraping_status(website):
#     page = requests.get(website)
#     return page.status_code


# a = scraping_status('https://www.google.co.in/')
# print(a)
# b = scraping_status('https://www.crunchbase.com/')
# print(b)

# # scraping_status(sys.arv[1])

# def system_control():
#     print('Press 1 for restart')
#     print('Press 2 for shutdown')
#     print('Press 3 for exit')

#     value = int(input('enter the value: '))

#     if value == 1:
#         os.system('shutdown /r /t 1')
#     elif value ==2:
#         os.system('shutdown /s /t 1')
#     else:
#         exit()


# def greeting(name,technology):
#     print(f'hello {name} so you work on {technology}')


# # greeting(sys.argv[1],sys.argv[2])

# #pip install smtplib


# def send_mail():
#     sender='parsen.jha@gmail.com'
#     password = 'vfrtpykqqqkhnreo'
#     server = smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     print('Handshake done')
#     server.starttls()
#     server.login(sender,password)
#     server.ehlo()

#     reciever = input('Enter reciever\'s address: ')
#     subject = 'Message from bot'
#     message = f'{subject} \n Hello This is a mail generated by Python Bot'
#     server.sendmail(sender,reciever,message)
#     print('Mail Sent')


# send_mail()

def var_length(*a):
    for _ in a:
        print(f'hello {_}')

data = ['dash','tarun','keshav','arsh','kartik','aayush','harish']

var_length(*data)

def terimaki(**data):
    for k,v in data.items():
        print(f'{k} ---> {v}')

values = {'name':'Prasenjit','surname':'jha','usp':'good in his things'}

terimaki(**values)