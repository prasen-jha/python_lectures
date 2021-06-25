class Employee:
    __num_employees =0
    raise_amt = 1.04

    def __init__(self,fname,pay,lname=''):
        self.fname = fname
        self.pay = pay
        self.lname = lname
        self._email = fname.lower()+'.'+lname.lower()+'@companyemail.com'
        Employee.__num_employees += 1

    def salary_raise(self):
        return int(self.pay*self.raise_amt)



    @property
    def email(self):
        return self._email

    # @email.setter
    # def email(self):

    @property
    def fullname(self):
        if self.lname is '':
            return f'{self.fname}'
        else:
            return f'{self.fname}  {self.lname}'

    @classmethod
    def total(cls):
        return cls.__num_employees
    
    def count_of_all(self):
        return self.__num_employees


    def __str__(self):
        return f'{self.fullname} is an employee with annual package of {int(self.pay*12)}'



class Developer(Employee):
    # child class developer inheriting from employee class
    raise_amt = 1.10

    def __init__(self,fname,pay,prog_lang,lname=''):
        super().__init__(fname,pay,lname='')
        self.prog_lang = prog_lang

    def salary_raise(self):
        return int(self.pay*self.raise_amt)

    def __str__(self):
        return f'{self.fullname} is programmer in {self.prog_lang} programming language'



print(Employee.total())
emp_1 = Employee('Prasenjit',950000)
print(emp_1.salary_raise())
dev_1 = Developer('Tarun',600000,'Python',lname='Verma')
print(dev_1.salary_raise())
print(dev_1.email)
print(dev_1)
print(Employee.total())
# print(emp_1)
# print(Employee.__num_employees)
print(help(dev_1))