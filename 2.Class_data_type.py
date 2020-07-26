'''

what is object?
it is real existance of class, we can create any number of object for a class

Referance variable:- the variable which is used to refer the object is called reference variable.


class represent data in variable:
    1.Instance variable(Object level variable)
    2.static variable(Class level variable)
    3.local variable(method level variable)

'''
class laptop:
    def __init__(self,companyName,RAM,processor,displaySize):
        self.companyName=companyName
        self.RAM=RAM
        self.processor=processor
        self.displaySize=displaySize

    def mediumRange(self):
        print("The laptop company name ",self.companyName)
        print("RAM",self.RAM)
        print("processor",self.processor)
        print("DisplaySize",self.displaySize)

sumit=laptop("HpCompany","8GB","Rayzen3","15 inch")  
sumit.mediumRange()      
    

