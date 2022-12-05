#hw 4 Leonard Blam 900086
#part 1
students = ["Chana", "Rachel", "Leah", "Julie", "Simone", "Danielle", "Ruth", "Lorry", "Janet"]

print("1a: ")
for x in students:
    print(x)

print("1b: ")
students.append("Tzippy")
for x in students:
    print(x)

print("1c: ")
students.remove("Rachel")
for x in students:
    print(x)

print("1d: ")
students.append("Nehama")
students.append("Sarit")
students.append("Michal")
students.append("Naomi")
for x in students:
    print(x)

print("1e: ")
students.remove("Chana")
students.remove("Julie")
students.remove("Simone")
for x in students:
    print(x)

print("1f: ")
students.sort()
for x in students:
    print(x)

print("1g: ")
count = 0
for x in students:
    if count <= 3:
        print(x)
    count += 1

print("1h: ")
students.reverse()
count = 0
for x in students:
    if count <= 3:
        print(x)
    count += 1

print()
print()
#part 2
print("2a: ")
first_word = "Sometimes, Usually, Frequently"
sentence1 = "I enjoy playing tennis"
sentence2 = "I see a movie"
sentence3 = "I learn the weekly Sedra"

word = first_word.split()
s1 = sentence1.split()
s2 = sentence2.split()
s3 = sentence3.split()

s1.insert(0,word[0])
s2.insert(0,word[1])
s3.insert(0,word[2])
st1 = st2 = st3 = ""
print("sentence 1: ")

for i in s1:
    st1 += i + " "
print(st1)

print("sentence 2: ")
for y in s2:
    st2 += y + " "
print(st2)

print("sentence 3: ")
for z in s3:
    st3 += z + " "

print(st3)

print("2b: ")

total = st1 + st2 + st3
total.upper()
total.lower()
print("Total: ")
print(total)
tot = total.split()
tot.sort()
for a in tot:
    print(a)
print(tot)
