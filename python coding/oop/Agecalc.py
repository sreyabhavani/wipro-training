from oop.myexception import AgeException


class Agecalculation():
    def voting_age_check(self,age):
        if age < 18:
            raise AgeException('Not Eligible to vote..')
        else:
            return True

    def pension_age_check(self,age):
        if age < 60:
            raise AgeException('not Eligible for pension')

