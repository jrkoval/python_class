class Person(object):
    def __init(self, name, age):
        self._name = name
        self._age = age
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        if age < 100:
            self._age = age
        else:
            self._age = 0
            

p1 = Person()
'''
first way we learned
__name ------> _Person__name
__age -----> _Person__age


'''

p1.name = "Amar"
p1.age = 30

print(p1.name, end=" ")
print(p1.age, end=" ")
