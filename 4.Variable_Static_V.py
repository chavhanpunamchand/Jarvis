'''
static variable:- The value of variable can not vary object to object called static variable.
                 - variable declare inside the class but outsite the method
                 - Total class only one copy of static variable will be created and share by all object
                 - Acesss by class name or objecct reference, but recommended to use class name.
eg. below
'''
class Test:
    x=10
    y=20
    def _init_(self):
        Test.a=100 #static variable not change
        self.f=100

    def m1(self):   # instance method 
        Test.d=100 
        self.x=100    

    @classmethod
    def addition(cls):
        #Test.b=50
        cls.b=50
        z=Test.x+Test.y
        print(z)
    @staticmethod    
    def m3():
        Test.c=25  

#print(Test.__dict__)
s1=Test()   
#print(Test.__dict__)
#s1.addition()
#print(Test.__dict__)
s1.m3()
Test.g=64
#print(Test.__dict__)
#print(s1.__dict__)
print(s1.g)

#s1.addition()    
