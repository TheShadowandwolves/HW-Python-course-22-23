
from ast import Pow
from cmath import sqrt
#library for the standard deviation
import numpy

# student class containing all grades and the name
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.math= grades["math"]
        self.physics = grades["physics"]
        self.chemistry= grades["chemistry"]
        self.psycho = grades["psycho"]
        self.history = grades["history"]
    # print function
    def prints(self):
        print(f'{self.name} had a grade of {self.science_Grade()} in his science courses and {self.social_grade()} in his social science courses. His overall average was {self.avg()} with a standard deviation of {self.deviation()}')
# avg of science grades
    def science_Grade(self):
        return ((self.math + self.physics + self.chemistry)/ 3)
    # avg of social grades
    def social_grade(self):
        return ((self.physics + self.history )/ 2)
# overall avg
    def avg(self):
        return ((self.science_Grade()+self.social_grade())/ 2)
    #deviation function using extern library
    def deviation(self):
        x1 = self.math
        x2 = self.physics
        x3 =  self.chemistry 
        x4 = self.psycho
        x5 = self.history
        return float(numpy.std([x1, x2, x3, x4, x5]))
    def points(self):
        math = physics = 6
        psycho = 5
        history = chemistry = 3
        avg = (math + physics + psycho + history + chemistry)/ 5
        message =f' {self.name} had an average of {self.science_Grade()} in his science courses and {self.social_grade()} in his social science courses. His weighted average was {avg}.'
        print(message)

def temperature(celc):
    return (9/5 * celc + 32)

def main():
    #part 1:

    grades = {"math": 89, "physics": 88, "chemistry": 90, "psycho": 80, "history": 80}
    student_a = Student("Jack Stein", grades)
    student_a.prints()

    #part 2:
    print("Enter student name: ")
    name = input()
    print("Enter grades by math, physics, chemistry, psychology and history: ")
    math = int(input())
    physics = int(input())
    chemi = int(input())
    psycho = int(input())
    hist = int(input())
    grades = {"math": math, "physics": physics, "chemistry": chemi, "psycho": psycho, "history": hist}
    student_b = Student(name, grades)
    student_b.prints()

    #part 3
    student_a.points()


    #part 4
    print("Enter a temperature in Celcius: ")
    temp = int(input())
    print(f'{temp} degrees Centigrade is equivalent to {temperature(temp)} degrees Fahrenheit.')

if __name__ == "__main__":
    main()