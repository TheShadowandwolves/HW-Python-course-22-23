import csv

print("part 1: ")
i = 1
sum = 0
avg = 0
while i <= 25:
    sum += i
    i +=1
avg = sum / 25
print(f'The sum is: {sum}')
print(f'The average is: {avg}')

print("part 2:")
sum = 0
avg = 0
odd = 0
i=0
while i <= 25:
    if i % 2:
        odd += 1
        sum += i
    i += 1
if not odd:
    odd = 1
avg = sum / odd
print(f'The sum is: {sum} and the average is: {avg}')

print("part 3: ")
i = 1
sum = 0
avg = 0
for i in range(1,25):
    sum += i
avg = sum / 25
print(f'The sum is: {sum}')
print(f'The average is: {avg}')

print("part 4: ")
sum = 0
avg = 0
odd = 0
for i in range(1,25):
    if i % 2:
        odd+=1
        sum += i
avg = sum / odd
print(f'The sum is: {sum} and the average is: {avg}')

print("part 5: ")

inp = input()
total = 0
count = 0
avg = 0
item = []
try:
    while inp != "Done":
        total += int(inp)
        count += 1
        item.append(inp)
        inp = input()
except:
    print("Missing input!")
avg = total / count
print(f'The total is: {total}, the average is: {avg}')
print("The numbers were: ")
print(item)

print("part 6: ")
inp = input()
fruit = []
while inp != "Done":
    fruit.append(inp)
    inp = input()

for f in fruit:
    for i in f:
        print(i, end="     ")
print()
print("part 7a: ")
dic = {}
with open('hw5q7.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #print(row)
            rows = []
            row[0].replace("\\", " ")
            rows = row[0].split()
            #print(rows)
            total_cost = int(rows[2]) * int(rows[3])
            print(f'\t Customer number {rows[0]} purchased {rows[3]} {rows[1]} for  {rows[2]} each, giving a total cost of ${total_cost} dollars.')
            try:
                if dic[rows[0]]:
                    dic[rows[0]] += total_cost
            except:
                dic[rows[0]] = total_cost    
            line_count += 1
    #print(f'Processed {line_count} lines.')
for i in dic:
    print(f'\t Customer number {i} had a total bill of ${dic[i]}')

print("part 8: ")
difwrds = []
slblen = []
with open('Gettysburg.txt') as csv_file2:
    csv_reader2 = csv.reader(csv_file2)
    file = csv_file2.read()
    file.replace(".", " ")
    file.replace(",", " ")
    list_file = file.split()
    print("part 8a: ")
    print(f'{list_file.__len__()} are in the file')
    list_file.sort()
    print(list_file)
    print("part 8b: ")
    difwrds.append(list_file[0])
    check = False
    for i in list_file:
        check = False
        for j in difwrds:
            if i == j:
                check = True
                break
        if check == False:
            difwrds.append(i)
    
    print(difwrds)
    print("part 8c: ")
    slblen = sorted(list_file, key=len)
    for i in slblen:
        print(f'{i} with length: {i.__len__()}')
    
    



