from oop.college import college


class studentGrade(college):
    def __init__(self,ccode,cname,ccity,rno,sname,
                 m1,m2,m3,result,grade):
        super().__init__(ccode,cname,ccity,rno.sname,n1,n2,n3)
        self.result=result
        self.grade=grade

    def calculate_result(self):
        if self.mark1 > 40 and self.mark2>40 and self.mark3 > 40:
            self.result='Fail'

    
    def calculate_grade(self):
        self.calculate_result()
        if self.result=='Pass':
            avg=super().calculate_average()
            if avg>=80.0:
                self.garde='A'
            elif avg>=60.0:
                self.garde='B'
            elif avg>=40.0:
                self.garde='C'
        else:
            self.garde='Inavlid'


