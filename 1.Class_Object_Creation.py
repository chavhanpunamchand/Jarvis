'''
class:- it is blue-print
objecct:- it is real intity
eg:- animal{
    dog{
        running
        jumping
    }
    cat
    goat
}
in above eg animal is class and dog is object and running and jumping is behaviour is nothing but the method and function.
syntax:
class className:
    "documenttation of string"--------doc. of the class
    variable: instance variable, static and local variable
    method: instance method, static method, class method

How to call:
variable(object creation)=className(parameter(initial parameter set in __init__ method))
variable(object).method_name()
'''
class studentMarks:
    ''' check the student marks '''
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks


    def check(self):
        print("Name of student:",self.name)
        print("Marks of student:",self.marks)    


s1=studentMarks("Punamchand",82) 
#s1.check()       


'''constructor:-
       In python constructor is used declare or initialize instance variable
       syntax:-
               def __init__(self,x,y):
                   self.instanceVariable=x
                   self.secondInstanceVariable=y

        Note:- self --It is default variable which is always pointing to the current object, variable, method.         

eg. if construtor not defined in python, but the by default python JVM creating the constructor     
       
'''
class Test:
    def __init__(self,name):
        self.name=name
        print("Calling constructor")

    def m1(self):
        print("M1 method execute")   

    def m2(self,name):
        print("M2 method calling",self.name)     

#t1=Test()        
#Test()
t2=Test("punamchand")
t2.m2("Punamchand")

