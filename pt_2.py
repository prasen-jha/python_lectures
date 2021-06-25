class Animal:
    limbs = 4
    species = 'canine'
    

    def __init__(self,name):
        self.name = name
        self._special_act = []

    def add_special(self,act):
        return self._special_act.append(act)

    def __str__(self):
        return f'{self.name} has these special activities{str(self._special_act)}'



a = Animal('Fido')
a.add_special('can speak hooman language')

print('----'*25)
b = Animal('Dino')
b.add_special('can cuss you in million ways')
print(b)
print(a)