class Person(object):
    def __init__(self,name,gender,age, salary):
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__salary= salary
    def show(self):
        print(self.__name, end=" ")
        print(self.__gender, end=" ")
        print(self.__age, end=" ")
        print
    def getName(self):
        return self.__name
    def getSalary(self):
        return self.__salary
    def getGender(self):
        return self.__gender
    def getAge(self):
        return self.__age
    def setName(age):
        self.__name = name
    def setAge(self):
        if self.age <100:
            self.__age = age
    def setSalary(self, salary):
        self.__salary = salary
    def setGender(self, salary):
        self.__gender = gender

fobj = open("C:/Users/rkovalch/Documents/python_class/employees.txt","r")

persons = []
for line in fobj:
    fields = line.split()
    name = fields[0]
    gender = fields[1]
    age = int(fields[2])
    salary = int(fields[3])
    person = Person(name,gender,age,salary)
    persons.append(person)

for person in persons:
    print(person.getName(), end=" ")
    print(person.getGender(), end=" ")
    print(person.getAge(), end=" ")
    print(person.getSalary(), end=" ")
    print()
#persons.sort(key=lambda item:item.getSalary())

persons.sort(key=lambda item:item.salary)
