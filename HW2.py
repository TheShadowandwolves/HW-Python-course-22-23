
#hw 2 leonard blam 900086
#part 1
print("part 1: ")
def string_call(string):
    string = string.replace("b", "")
    first_name = string.split(",")[1]
    last_name = string.split(",")[0]
    salary = string.split(",")[2]
    print(f'{first_name} {last_name} owes ${salary}')
user_string = "Cohen,bMr.bJohn,b47.38b"
string_call(user_string)
print("part 2: ")
#part 2

#count how many vowels are in a string
def count_vowels(string):
    vowels = 0
    for i in string:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            vowels += 1
    return vowels

#call count_vowels function on user_string
print(count_vowels(user_string))

#part 3
print("part 3: ")

string_call("Cohen,bMr.bJohn,b47.38b")
string_call("Tubolsi,bMs.bDevora,b53.78b")
string_call("Fried,bDr.bZev,b142.45b")

#part 4
# print("part 4: ")
# didn't understand the question
