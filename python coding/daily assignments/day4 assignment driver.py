'''from day4_assignment import Bankaccount

acc_no=int(input('Enter acc no:'))
name=input('Enter name:')
balance=float(input('Enter balance:'))

acc = Bankaccount(acc_no,name,balance)

print('\n Account created sucessfully',acc.display())

deposit_amount=float(input('Enter amount to deposit:'))
acc.deposit(deposit_amount)
withdraw_amount=float(input('Enter amount to withdraw:'))
acc.withdraw(withdraw_amount)

print('\n Final Account Details:',acc.get_details())
'''

from day4_assignment import Employee

emp_id=int(input('Enter id :'))
name=input('Enter you name:')
salary=float(input('Enter your salary:'))

emp=Employee(emp_id,name,salary)
percent=float(input('\n Enter hike percentage:'))
emp.give_hike(percent)

print('\n Hike after salary:',emp.get_details())

