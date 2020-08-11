class StudentInfo:

    def m1(self, sid, snm, sag, semail):  # these props will be avaiable for all objects of this class
        self.studId = sid
        self.studName = snm
        self.studAge = sag
        self.studEmail = semail

    def display(self):

        print(''' Student Id:{}
                   Student Name:{}
                   student Age:{}
                   Student Email:{}           
        '''.format(self.studId,self.studName,self.studAge,self.studEmail)  )  

s1 = StudentInfo()  #there is default constructor   --> initialization part-->
s1.m1(10,"ABC",29,"ABC@gmail.com") # one line--> extra-->
s1.display() #one extra line
#print(data)
#print(s1)
s11 = StudentInfo()  #there is default constructor   --> initialization part-->

