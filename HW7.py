import os

dic = {"134": "John", "253": "Berger", "456": "Levi", "654": "Fried"}
print(dic)

print("part 1b:")

person1 = {"ID": 134, "First Name": "John", "Last Name": "Cohen", "Average": 85.4, "Points": 65}
person2 = {"ID": 253, "First Name": "Sara", "Last Name": "Berger", "Average": 73.9, "Points": 47}
person3 = {"ID": 456, "First Name": "Chana", "Last Name": "Levi", "Average": 94.6, "Points": 88}
person4 = {"ID": 654, "First Name": "Yochai", "Last Name": "Fried", "Average": 88.9, "Points": 102}
arr = [person1, person2, person3, person4]

tx = input("Enter ID: ")
#compare if id key is same as input

if tx == arr[0]:
    print(f'{person1["First Name"]} {person1["Last Name"]}, ID number {person1["ID"]}, has accumulated {person1["Points"]} with an average of {person1["Average"]}')
elif tx == arr[1]:
    print(f'{person2["First Name"]} {person2["Last Name"]}, ID number {person2["ID"]}, has accumulated {person2["Points"]} with an average of {person2["Average"]}')
elif tx == arr[2]:
    print(f'{person3["First Name"]} {person3["Last Name"]}, ID number {person3["ID"]}, has accumulated {person3["Points"]} with an average of {person3["Average"]}')
elif tx == arr[3]:
    print(f'{person4["First Name"]} {person4["Last Name"]}, ID number {person4["ID"]}, has accumulated {person4["Points"]} with an average of {person4["Average"]}')

print("part 1c:")
for person in arr:
    print(person)

print("part 1d:")
for person in arr:
    print(person["ID"], person["First Name"], person["Last Name"], person["Average"], person["Points"])

print("part 1e:")
for person in arr:
    print(person.keys())



print("part 1f:")

with open('Averages.csv', 'r+') as file:
    fil = file.readlines()
    for line in fil:
        new_line = line.split(',')
        new_person = {"ID": new_line[0], "First Name": new_line[1], "Last Name": new_line[2], "Average": new_line[3], "Points": new_line[4]}
        arr.append(new_person)
    
print("part 1g:")

for person in arr:
    print(person["ID"], person["First Name"], person["Last Name"], person["Average"], person["Points"])


print("part 2:")
# open the file for reading
with open('words.txt', 'r') as f:
   # create an empty dictionary to store the word counts
   word_counts = {}

   # read each line of the file
   for line in f:
       # split the line into words
       words = line.split()

       # iterate through the words
       for word in words:
           # if the word is not already in the dictionary, add it as a key
           # with a value of 1
           if word not in word_counts:
               word_counts[word] = 1
           # if the word is already in the dictionary, increment its value
           else:
               word_counts[word] += 1

   # sort the dictionary by key
   sorted_word_counts = sorted(word_counts.items())

   # print each key-value pair in the sorted dictionary
   for word, count in sorted_word_counts:
       print(word, count)

print("part 3:")
# open the file containing the Gettysburg Address
with open('gettysburg_address.txt', 'r') as f:
   # create an empty dictionary to store the word counts
   word_counts = {}

   # read the contents of the file into a string
   contents = f.read()

   # split the contents into words
   words = contents.split()

   # iterate through the words
   for word in words:
       # if the word is not already in the dictionary, add it as a key
       # with a value of 1
       if word not in word_counts:
           word_counts[word] = 1
       # if the word is already in the dictionary, increment its value
       else:
           word_counts[word] += 1

   # prompt the user to input a word
   user_input = input("Enter a word (enter 'Done' to stop): ")

   # loop until the user inputs 'Done'
   while user_input != 'Done':
       # if the word is in the dictionary, print its frequency
       if user_input in word_counts:
           print(f"{user_input}: {word_counts[user_input]}")
       # if the word is not in the dictionary, print a message
       else:
           print(f"{user_input} not found in the text.")

       # prompt the user to input another word
       user_input = input("Enter a word (enter 'Done' to stop): ")

print("part 4:")
import statistics
import csv

# create empty dictionaries to store the student and course data
students = {}
courses = {}

# read the student file into the students dictionary
with open('student_file.csv', 'r') as f:
   reader = csv.reader(f)
   next(reader)  # skip the header row
   for row in reader:
       student_id = row[0]
       name = row[1]
       address = row[2]
       average = float(row[3])
       students[student_id] = {'name': name, 'address': address, 'average': average}

# read the course file into the courses dictionary
with open('course_file.csv', 'r') as f:
   reader = csv.reader(f)
   next(reader)  # skip the header row
   for row in reader:
       course_number = row[0]
       name = row[1]
       credits = int(row[2])
       courses[course_number] = {'name': name, 'credits': credits}

# read the registration file and calculate the overall average and standard deviation for each student
with open('registration_file.csv', 'r') as f:
   reader = csv.reader(f)
   next(reader)  # skip the header row
   current_student = None
   grades = []
   for row in reader:
       student_id = row[0]
       course_number = row[1]
       grade = float(row[2])

       # if we have reached a new student, calculate and print the overall average and standard deviation
       if student_id != current_student:
           if current_student is not None:
               average = statistics.mean(grades)
               stddev = statistics.stdev(grades)
               name = students[current_student]['name']
               print(f"{name}'s overall (weighted) average was {average:.1f} with a standard deviation of {stddev:.1f}.")
           current_student = student_id
           grades = []

       # add the grade to the list
       grades.append(grade * courses[course_number]['credits'])

# calculate and print the overall average and standard deviation for the last student
average = statistics.mean(grades)
stddev = statistics.stdev(grades)
name = students[current_student]['name']
print(f"{name}'s overall (weighted) average was {average:.1f} with a standard deviation of {stddev:.1f}.")
