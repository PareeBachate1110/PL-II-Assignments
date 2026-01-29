class bank_acc:
    def __init__(self,acc_no,balance,amt_dep,amt_withd,new_bal):
        self.acc_no=acc_no
        self.balance=balance
        self.amt_dep=amt_dep
        self.amt_withd=amt_withd
        self.new_bal=new_bal

    def deposit(self):
        print("Account No. : ",self.acc_no)
        print("Balance : ",self.balance)
        print("Amount Deposited : ",self.amt_dep)
        print("Updated Balance : ",self.new_bal)
        print("-----------------------------------------------")

    def withdraw(self):
        print("Account No. : ",self.acc_no)
        print("Balance : ",self.balance)
        print("Amount Withdrawn : ",self.amt_withd)
        print("Updated Balance : ",self.new_bal)
        print("-----------------------------------------------")

    def check_bal(self):
        print("Account No. : ",self.acc_no)
        print("Balance : ",self.balance)
        print("-----------------------------------------------")
       

acc1=bank_acc("ABC0001","50000","5000","","55000")
acc1.deposit()

acc2=bank_acc("ABC0002","10000","","500","9500")
acc2.withdraw()

acc3=bank_acc("ABC0003","1000000","","","")
acc3.check_bal()