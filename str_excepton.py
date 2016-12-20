class NotStringItem(Exception):
    def __init__(self,arg):
        Exception.__init__(self,arg)
        self.arg = arg
    def __str__(self):
        return 'Not a string %s' %(self.arg)
class StringList(list):
    def append(self,item):
        if type(item) == str:
            list.append(self,item)
        else:
            raise NotStringItem(item)

class alpha:
    def __str__(self):
         return("This is the alpha function")
a = alpha()
print(a)

s1 = StringList()
print("here 1")
s1.append([3.14,45,56])
print("here 2")
s1.insert(0, 'perl')
print("here 3")
print(s1)
