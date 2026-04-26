from oop.college import college


class Teacher(college):
    def __init__(self,ccode,cname,ccity,empid,tn,de,bp):
        super().__init__(ccode,cname,ccity)
        self.empid=eid
        self.dept=de
        self.tname=tn
        self.basicpay=bp

    def calculate_salary(self):
        return self.basicpay + (self.basicpay*0.2) - (self.basicpay*0.08)

