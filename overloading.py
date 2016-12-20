def add(a,b):
    return a + b
#python supports dynamic typing
print(add(20,30))
print(add(3.14,2.25))
print(add('perl', 'python'))

#compiler does syntax and grammar check and translates to some other

#every function in python is runtime polymorphic
# this is called type overloading

#Next length overloading
#C++ has to write 2 functions, 1st function takes one arg, 2nd function takes
#two and decided when call which to use.

#but python has default arguments
def addd(a=10, b=20)
    return a+b

print(add(13))
print(add(13,14))

#also if you only want to pass to one arg and use the defaults for the others
print(add(a=33, b=66))
print(add(b=222))
