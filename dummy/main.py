print("MAIN FILE")
from merofunctions import *

result_mul = mul(15,3)
result_add = add(4,5)
print(result_mul)

result_div = divide(5,0)
print(result_div)
print("TRANSACTION COMPLETE")


class Person():
    job = None
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def about_me(self):
        print(f"My name is {self.name} and I am {self.age} , My Job is {self.job}")
        print("My name is " + self.name + " and I am " + str(self.age),"MY JOOB",self.job)

    def add_job(self,job):
        self.job = job

person_1 = Person("RAM",45)
person_1.about_me()
person_1.add_job("TEACHER")
person_1.about_me()


