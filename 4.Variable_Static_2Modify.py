'''
Declare static variable and accessing static variable

'''
class test:
    x=20 # define static variable

    @classmethod
    def m1(cls):
        cls.x=30

    @staticmethod
    def m2():
        test.x=40

'''print(test.x)
test.m1()
print(test.x)
test.m2()
print(test.x)
s1=test()
s1.m1()
print(test.__dict__)'''

#e.g :- Please check

class Test:
    a=10 #Static value declaration
    def __init__(self):
        self.b=20
        del Test.a

    def m3(self):
        Test.c=30
        #del Test.b    

    @classmethod
    def m4(cls):
        cls.d=40
        del cls.c
    @staticmethod
    def m5():
        Test.e=50
        del Test.d

print(Test.__dict__) 
t1=Test()
print("\n")
print(Test.__dict__) 
t1.m3()
print("\n")
print(Test.__dict__) 
t1.m4()
print("\n")
print(Test.__dict__) 
t1.m5()
print("\n")
print(Test.__dict__) 
Test.f=65
print("\n")
print(Test.__dict__) 
del Test.e
print("\n")
print(Test.__dict__) 


    


