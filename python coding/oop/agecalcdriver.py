from oop.Agecalc import Agecalculation
from oop.myexception import AgeException

age=int(input('Age:'))

aobj=Agecalculation()

try:
    aobj.voting_age_check(age)
o
except AgeException as ae:
    print(ae)

else:
    print('Eligible.Contact next step...')