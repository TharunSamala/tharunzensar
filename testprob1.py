class BankInfo:
    balance=0
    def Account(self,m,n):
        self.balance=m
        return self.balance
    def deposit(self,x):
        self.balance+=x
        return self.balance

    def withdrawl(self,y):
        self.balance-=y
        return self.balance
    def AddNominee(self,name):
        self.b=name
        list=[]
        list.append(self.b)
acct1=BankInfo()
acct2=BankInfo()
acct1.Account(5000,"Sachin")
acct1.deposit(1000)
acct1.withdrawl(1000)
acct2.Account(3000,'Ali')
acct2.deposit(500)
acct2.withdrawl(250)
if(acct1 == acct2):
    print("Thay have equal balance")
else:
    print("Thay have different balance")


if(acct1 != acct2):
    print("Oops!!! they are not equal")
else:
    print("wow!!!  they are equal")


if(acct2 > acct1):
    print("acct2 should pay more tax")
else:
    print("acct1 should pay normal tax")

if(acct2 < acct1):
    print("Sponsor for two children")
else:
    print("Start an Orphanage")

if(acct2 >= acct1):
    print("Go On Europe Trip")
else:
    print("Go for an excursion")


if(acct2 <= acct1):
    print("We can have coffee")
else:
    print("We can have meals")
acct1.AddNominee("Ranjini")
acct1.AddNominee("Ragini")
acct1.AddNominee("Malini")
acct1.AddNominee("Rukmini")
for nom in list:
    print(nom)










