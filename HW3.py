#part 1a
print("Part 1: Enter 2 strings: ")
first = input()
second = input()
while first == second:
    print("The two strings are the same")
    break
else:
    print("The two strings are different")
#part 1b
while first[0] == second[0] or first[1] == second[1]:
    print("The two strings have the same first letter")
    break
else:
    print("The two strings do not have the same first letter")
#part 1c
while first[0] == second[1] or first[1] == second[0]:
    print("the first letter of the first string is the same as the second letter of the second string")
    break
else:
    print("the first letter of the first string is not the same as the second letter of the second string")

#part 2
print("part 2: ")
class Student:
    def __init__(self, id,served, degree, tall, weight):
        self.id = id
        self.served = served
        self.degree = degree
        self.tall = tall
        self.weight = weight
        self.legit = False
    def __repr__(self) -> str:
        while self.served == True:
            while self.degree >= 85:
                while self.tall > 1.70:
                    while self.weight > 60:
                        self.legit = True
                        break
                    break
                break
            break
        return f'Student ({self.id}) is acceptable as a security person: {self.legit}'

alex = Student(123456789, True, 90, 1.80, 80)
felix = Student(987654321, True, 80, 1.60, 50)
print(alex)
print(felix)
#part 3
print("part 3: ")
a = input("Enter a number: ")
b = input("Enter a number: ")
#determinates the quotient and remainder
quotient = int(a) // int(b)
remainder = int(a) % int(b)
print(f'The numbers: {a} and {b}: The quotient is {quotient} and the remainder is {remainder}')

#part 4
#redo part 1 with try and except
print("part 4: ")
try:
    print("Part 1: Enter 2 numbers: ")
    first = int(input())
    second = int(input())
    while first == second:
        print("The two strings are the same")
        break
    #part 1b
    while first[0] == second[0] or first[1] == second[1]:
        print("The two strings have the same first letter")
        break
    #part 1c
    while first[0] == second[1] or first[1] == second[0]:
        print("the first letter of the first string is the same as the second letter of the second string")
        break
except:
    print("Error: please enter 2 numbers")

#part 5
print("part 5: ")
age = int(input("Enter your age: "))
martial_status = bool(input("Enter your martial status: "))
children = bool(input("Do you have children? "))
if age >= 30 and martial_status == True and children == True:
    print("You are entitled for cheap mortgage")
else:
    print("You are not entitled for cheap mortgage")

#part 6
print("part 6: ")
print("Enter your spend amount: ")
spend = int(input())
if spend >= 500 and spend < 1000:
    discount = spend - 0.1 * spend
elif spend >= 1000 and spend < 2000:
    discount = spend - 0.2 * spend
elif spend >= 2000:
    discount = spend - 0.25 * spend
elif spend > 3000:
    discount = spend - ((spend * 0.3 + (spend - 2000) * 0.4))

print(f'You amount before discount is {spend} and your amount after discount is {discount}')

#Result:
# PS D:\Dokumente\Python> python HW3.py
# Part 1: Enter 2 strings: 
# hello
# hi
# The two strings are different
# The two strings have the same first letter
# the first letter of the first string is not the same as the second letter of the second string
# part 2:
# Student (123456789) is acceptable as a security person: True
# Student (987654321) is acceptable as a security person: False
# part 3:
# Enter a number: 20
# Enter a number: 10
# The numbers: 20 and 10: The quotient is 2 and the remainder is 0
# part 4:
# Part 1: Enter 2 numbers:
# 20
# e
# Error: please enter 2 numbers
# part 5:
# Enter your age: 31
# Enter your martial status: True
# Do you have children? Yes
# You are entitled for cheap mortgage
# part 6:
# Enter your spend amount:
# 1000
# You amount before discount is 1000 and your amount after discount is 800.0