


'''class Bankaccount:
    def __init__(self,acc_no,name,balance):
        self.__acc_no=acc_no
        self.__name=name
        self.__balance=balance

    def get_details(self):
        return f'Account no:{self.__acc_no}, name:{self.__name},balance:{self.__balance}'

    def get_acc_no(self):
        return self.__acc_no


    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    def set_name(self,name):
        self.__name=name

    def set_bal(self,balance):
        self.__balance=balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print('Amount deposited')
        else:
            print('Invalid ammount')

    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print('Withdraw sucessfully')
        else:
            print('Insufficinet balance')

    def display(self):
        print('Acc no:',self.__acc_no)
        print('Name:',self.__name)
        print('Balance:',self.__balance)
'''



#employee management system
class Employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary

    def get_details(self):
        return f'Employee details:{self.emp_id}, \n name:{self.name},\n salary:{self.salary}'



    def get_emp_id(self):
        return self.emp_id


    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    def set_name(self,name):
        self.name=name

    def set_salary(self,salary):
        self.salary=salary

    def deposit(self):
            print('Employee id:',self.emp_id)
            print('Name:',self.name)
            print('salary:',self.salary)

    def give_hike(self,percent):
        if percent>0:
            self.salary+=self.salary*percent/100
            print('Hike applied')
        else:
            print('Hike not applied')


