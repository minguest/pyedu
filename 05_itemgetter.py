from operator import itemgetter

students =[
    ("jane", 22, 'A'),
    ("dave", 90, 'E'),
    ("sally", 2, 'AA'),
]

result= sorted(students, key=itemgetter(2))
# print(result)

students =[
    {"name":"jane", "age":"3", "grade":"A"},
    {"name":"dave", "age":"6", "grade":"F"},
    {"name":"sally","age":"8", "grade":"Z"},
]

result= sorted(students, key=itemgetter("name"))
# print(result)

from operator import attrgetter

class Student:
    def __init__(self,name , age, grade):
        self.name= name
        self.age=age
        self.grade= grade
    
    def __repr__(self):
        return f'{self.name}:{self.age}:{self.grade}'

a = Student('jane', 22, 'H')
b = Student('dave', 12, 'B')
c = Student('sally', 82, 'R')

print(a.age, a.name, a.grade)
print(a)

students= [
    a,
    b,
    c
]

result= sorted(students, key=attrgetter('age'))
print(result)