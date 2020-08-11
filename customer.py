import sys

print("This is block execution")


sys.exit(0)

class Customer:

    def __init__(self, cid, cnm): # 182x
        self.custId = cid
        self.custName = cnm

    '''def __init__(self,cid,cnm,cag,cemail,cbal): #1834x
        self.custId = cid
        self.custName = cnm
        self.custAge = cag
        self.custEmail = cemail
        self.custBalance = cbal'''

#c2 = Customer(10,"ABC") # this wont work
#print(c2)
c1 = Customer(10,"ABC",29,"abd@gmail.com",50.52)
print(c1)