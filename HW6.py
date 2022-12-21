#HW 6 Python
# Leonard Blam 900086
# this code doesn't include the csv files needed to run it


print("part1: ")
# Define a function to transform a numeric grade into a letter grade
def grade_to_letter(grade):
  # Check the numeric grade and return the corresponding letter grade
  if grade >= 90:
    return "A"
  elif grade >= 80:
    return "B"
  elif grade >= 70:
    return "C"
  elif grade >= 60:
    return "D"
  else:
    return "F"

# Loop indefinitely
while True:
  # Prompt the user for a grade
  grade = input("Enter a grade (or 'Done' to quit): ")

  # Check if the user entered 'Done'
  if grade == "Done":
    # If so, stop the loop
    break

  # Otherwise, convert the grade to a number
  grade = int(grade)

  # Check if the grade is valid
  if grade >= 0 and grade <= 100:
    # If so, convert the grade to a letter grade
    letter_grade = grade_to_letter(grade)

    # Print the result
    print(f"The letter grade is: {letter_grade}")
  else:
    # If the grade is not valid, print an error message
    print("Invalid grade")


print("part2: ")
def calculate_pay(hours_worked, pay_per_hour):
    # Calculate the employee's regular pay
    regular_pay = hours_worked * pay_per_hour
    
    # Calculate the employee's overtime pay
    overtime_hours = 0
    overtime_pay = 0
    if hours_worked > 60:
        # The employee worked more than 60 hours, so they get paid 200% for each hour above 60
        overtime_hours = hours_worked - 60
        overtime_pay = overtime_hours * pay_per_hour * 2
    elif hours_worked > 40:
        # The employee worked more than 40 hours, but not more than 60, so they get paid 150% for each hour above 40
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * pay_per_hour * 1.5
    
    # Calculate the employee's total pay
    total_pay = regular_pay + overtime_pay
    
    return total_pay

# Continuously prompt the user for input until they enter 'Done'
while True:
    hours_worked = input("Enter the number of hours worked (or 'Done' to quit): ")
    if hours_worked == "Done":
        break
    pay_per_hour = input("Enter the employee's pay per hour: ")
    total_pay = calculate_pay(hours_worked, pay_per_hour)
    print(f"The employee's total pay is ${total_pay:.2f}")

print("part3: ")
print("This is one version: ")
import csv

def calculate_pay(hours_worked, pay_per_hour):
    # Calculate the employee's regular pay
    regular_pay = hours_worked * pay_per_hour
    
    # Calculate the employee's overtime pay
    overtime_hours = 0
    overtime_pay = 0
    if hours_worked > 60:
        # The employee worked more than 60 hours, so they get paid 200% for each hour above 60
        overtime_hours = hours_worked - 60
        overtime_pay = overtime_hours * pay_per_hour * 2
    elif hours_worked > 40:
        # The employee worked more than 40 hours, but not more than 60, so they get paid 150% for each hour above 40
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * pay_per_hour * 1.5
    
    # Calculate the employee's total pay
    total_pay = regular_pay + overtime_pay
    
    return total_pay

# Open the CSV file and read each employee's information
with open('employees.csv') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        # Calculate the employee's total pay
        name = row[0]
        hours_worked = int(row[1])
        pay_per_hour = int(row[2])
        total_pay = calculate_pay(hours_worked, pay_per_hour)
        
        # Print out the employee's gross salary
        print(f"{name} worked {hours_worked} hours at ${pay_per_hour} per hour and received a gross salary of ${total_pay:.2f}.")

print("part3: ")
print("This is another version: ")
def calculate_salary(hours_worked, pay_per_hour):
  gross_salary = hours_worked * pay_per_hour
  return gross_salary

# Open the csv file and read the data
with open("employees.csv", "r") as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    name = row[0]
    hours_worked = row[1]
    pay_per_hour = row[2]

    # Calculate the salary and print it out in the desired format
    salary = calculate_salary(hours_worked, pay_per_hour)
    print("{} worked {} hours at ${} per hour and received a gross salary of ${}.".format(name, hours_worked, pay_per_hour, salary))

#This code assumes that the csv file has a header row, 
# with the column names "name", "hours_worked", and "pay_per_hour".
#  It also assumes that the data in the columns is formatted as strings, so you may need to 
# convert the hours_worked and pay_per_hour values to numbers before calling the calculate_salary function.

print("part4: ")
import csv

def calculate_salary(hours_worked, pay_per_hour):
  gross_salary = hours_worked * pay_per_hour
  return gross_salary

def calculate_tax(gross_salary, married, num_children):
  # Calculate the tax rate based on the marital status and number of children
  tax_rate = 0.25
  if married == "yes":
    tax_rate -= 0.05
  tax_rate -= 0.02 * num_children

  # Calculate the net salary by subtracting the tax from the gross salary
  net_salary = gross_salary - (gross_salary * tax_rate)
  return net_salary

# Open the csv file and read the data
with open("employees.csv", "r") as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    name = row[0]
    hours_worked = row[1]
    pay_per_hour = row[2]
    married = row[3]
    num_children = row[4]

    # Calculate the gross salary and net salary
    gross_salary = calculate_salary(hours_worked, pay_per_hour)
    net_salary = calculate_tax(gross_salary, married, num_children)

    # Print the results in the desired format
    print("{} worked {} hours at ${} per hour and received a gross salary of ${}. After taxes, their net salary is ${}.".format(name, hours_worked, pay_per_hour, gross_salary, net_salary))

#This code assumes that the csv file has a header row, with the 
# column names "name", "hours_worked", "pay_per_hour", "married", and "num_children". It also assumes 
# that the data in the columns is formatted as strings, so you may need to convert
#  the hours_worked, pay_per_hour, and num_children values to numbers before calling the calculate_salary and calculate_tax functions.

print("part5: ")

import string

def initialize():
  # Read the text of the Gettysburg Address into a string
  with open("gettysburg_address.txt", "r") as textfile:
    gettysburg_address = textfile.read()

  return gettysburg_address

def delete_punctuation(text):
  # Remove punctuation from the text using the translate method
  translator = str.maketrans("", "", string.punctuation)
  text = text.translate(translator)

  return text

def determine_number(text):
  # Split the text into a list of words
  words = text.split()

  return words, len(words)

def determine_unique_words(words):
  # Create a list of unique words
  unique_words = set(words)

  return unique_words

def order_alphabetically(words):
  # Sort the words alphabetically and print them out
  words = list(words)
  words.sort()
  print("The words in the Gettysburg Address, arranged alphabetically:")
  print(words)

def order_by_length(words):
  # Sort the words by length in descending order and print them out
  words.sort(key=len, reverse=True)
  print("The unique words in the Gettysburg Address, sorted from longest to shortest:")
  for word in words:
    print("{} ({} characters)".format(word, len(word)))

# main program
txt = initialize()
txt_del = delete_punctuation(txt)
txt_words, num_words = determine_number(txt_del)
print("The Gettysburg Address has {} words.".format(num_words))
txt_unique_words = determine_unique_words(txt_words)
order_alphabetically(txt_unique_words)
order_by_length(txt_unique_words)
