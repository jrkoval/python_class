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
    
class Employee(Person):
    def __init__(self, name, gender, age, salary):
        # self below is the object of employee not person
        # thename, gender and age are attached to the employee
        # object not the person
        Person.__init__(self, name, gender, age)
        self.__salary = salary

    #over-riding
    def show(self):
        Person.show(self)
        print(self.__salary)

#e1 = Employee("amar","m",35,65000)
#e1.show()
#suprising for C++/Java programmers
#private, protected
#Python was designed for non-programmers like mathmeticians, statisticians
# etc. so the library was kept simple
#e1.name = 'mark'
#any attribute that starts with __ will not be able to be accessed directly

#print(dir(e1))
# can access this way
#print(e1._Person__name)
# so the attributes are called pseudo private attributes
#print(e1.getName())
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
persons.sort(key=lambda item:item[1])

