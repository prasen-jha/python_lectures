import datetime

class Human:
    SPECIES = 'Human'

    # def __init__(self):
    #     pass
    _pets=[]
    def __init__(self,name,gender,ethnicity,can_walk=True,):
        self.name = name
        self.gender = gender
        self.ethnicity = ethnicity
        self.can_walk = can_walk
        # self.birthdate = birthdate

    # def age(self):
    #     if hasattr(self,'_age'):
    #         return self._age
    #     today = datetime.date.today()
    #     age = today.year - self.birthdate.year

    #     if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
    #         age -= 1

        # return age
    def add_pet(self,pet):
        return self._pets.append(pet)

    @property
    def walk(self):
        if self.can_walk:
            print('%s can walk'%self.name)
        else:
            print('cannot walk')

    def create_attr(self,attr,value):
        setattr(self,attr,value)


    #including dunder methods
    def __str__(self):
        return '%s is an object of %s'%(self.name,self.SPECIES)
    
    def __repr__(self):
        return "{'name':%s,'gender':%s,'species':%s}"%(self.name,self.gender,self.SPECIES)


a = Human(gender='Male',ethnicity='South East Asian',name = 'Anurag',can_walk=False)

# b = Human('dash','M','omnipresent')
print(a.add_pet('doggo'))
print(a._pets)



# keys = ['name','gender','ethnicity','color']

# for k in keys:
#     print(getattr(a,k,None))

# setattr(a,'color','Red')
# print(hasattr(a,'color'))


