class student:
    def __init__(self,sid,sname,sdept,saddress,sPercentage):
        self.StdId=sid
        self.stdName=sname
        self.stdDept=sdept
        self.stdAddress=saddress
        self.stdPercentage=sPercentage

    def __str__(self):     #str fuction used for represent the object 
        return f'''Student ID: {self.StdId}
                   Student Name: {self.stdName}
                   Student Depatment: {self.stdDept}
                   Student Address: {self.stdAddress}
                   Student Percentage: {self.stdPercentage}
                ''' 
    def __repr__(self):     #  when u want to print group of collegues
        return str(self)    #str --> one by one list items


s1=student(101,"Punamchand","Information Technology","Tq.Pusad Dist. Yavatmal",84)  
s2=student(102,"Ravi","Computer Science","Tq.Digras Dist. Yavatmal",78)  
l=[s1,s2]
#print(s1)      
print(l)      
