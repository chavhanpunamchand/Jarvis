'''
type of variable in python
1.Instance variable(Object level)
2.static variable(class level)
3.local variable(Method level)

1. Instance variable :- the value of variable vary from object to object is called instance variable

for every object having a separate copy of instance variable will be created

instance variable declearation
'''
#1. inside constructor by using self keyword

class family:
    def __init__(self,x,y,z):
        self.name=x #inside the constructor
        self.age=y
        self.relation=z

    def workStatus(self,work):
        self.work=work #access in the class by using self variable and outside the class by object referance
        del self.name #delete by self kayword

    def display(self):
        print("Punamchand is {} \n and  {}\n work:{}\n".format(self.relation, self.age,self.work))  

s2=family("Ravi",24,"brother")#one object delation and creation not affected to another object
s2.workStatus("Teacher")
s2.c="Ramakant"
s1=family("Rajesh",12,"father")         
s1.workStatus("Student") 
s1.d=40 
#print(s1.name) 
s1.display()
del s1.relation #del by using the referance variable 
print(s1.age) #access variable outside the class by object reference
print(s1.__dict__)
print(s2.__dict__)# every object having instance or self copy


