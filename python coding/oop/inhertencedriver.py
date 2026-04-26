from pickletools import read_stringnl_noescape

from oop.Student import student
from oop.college import college

cc =int(input('c code:'))
cn=input('c name:')
ci=input('city:')
rno=int(input('Roll No:'))
sn=input('S Name:')
m1=int(input('M1:'))
m2=int(input('M2:'))
m3=int(input('M3:'))
eid=int(input('Eid:'))
tn=input('Teach name:')
de=input('Dept Name:')
bp=float(input('Bp:'))


#project=college(ccode=cc,cname=cn,ccity=ci)

#project.welcome_message()
#project.display_college_details()

project=studentgrade(ccode=cc , cname=cn, ccity=cc , rno=rno,sname=sn,m1=m1,m2=m2,m3=m3)

project.welcome_message()
project.display_college_details()
print(f'Roll no:{project.rollno} \t Name: {project.stuname}'
      f'Total:{project.calculate_total()} \n Average: {project.calculate_average}')
project.calculate_grade()
print(f'Result:{project.result} \t Grade:{project.grade}')


teach=Teacher(ccode=cc,cname=cn,ccity=ci,eid=eid,tn=tn,de=de,bp=bp)
print(f'Eid:{teach.empid} \t Name:{teach.name} \t Dept:{teach.dept}')
print(f'salary:{teach.calculate_salary}')