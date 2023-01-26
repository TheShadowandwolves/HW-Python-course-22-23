print("part 1a")
tuple_items = ('fish', 'cheese', 'eggs', 'toast', 'cake')
print(tuple_items)

print("part 1b")
tuple_items = ('fish', 'cheese', 'eggs', 'toast', 'cake', 'ice cream')
print(tuple_items)

print("part 1c")
tuple_items = ('fish', 'cheese', 'scrambled eggs', 'toast', 'cake')
print(tuple_items)

print("part 1d")
tuple_items = ('salmon', 'trout', 'cod', 'toast', ('chocolate', 'vanilla', 'carrot', 'apple', 'cherry'), ('hard cheese', 'cream cheese'), 'melon', 'fruit salad', 'pizza', 'grapefruit')
print(tuple_items)

print("part 1e")
menu = [
('salmon', 12.99, 'main dish'),
('trout', 10.99, 'main dish'),
('cod', 15.99, 'main dish'),
('toast', 2.99, 'appetizer'),
('chocolate cake', 4.99, 'dessert'),
('vanilla cake', 4.99, 'dessert'),
('carrot cake', 4.99, 'dessert'),
('apple pie', 5.99, 'dessert'),
('cherry pie', 5.99, 'dessert'),
('hard cheese', 6.99, 'appetizer'),
('cream cheese', 4.99, 'appetizer'),
('melon', 2.99, 'dessert'),
('fruit salad', 5.99, 'dessert'),
('pizza', 9.99, 'main dish'),
('grapefruit', 2.99, 'dessert')
]

for item in menu:
    print(item)

print("part 1f")
menu = [
('salmon', 12.99, 'main dish'),
('trout', 10.99, 'main dish'),
('cod', 15.99, 'main dish'),
('toast', 2.99, 'appetizer'),
('chocolate cake', 4.99, 'dessert'),
('vanilla cake', 4.99, 'dessert'),
('carrot cake', 4.99, 'dessert'),
('apple pie', 5.99, 'dessert'),
('cherry pie', 5.99, 'dessert'),
('hard cheese', 6.99, 'appetizer'),
('cream cheese', 4.99, 'appetizer'),
('melon', 2.99, 'dessert'),
('fruit salad', 5.99, 'dessert'),
('pizza', 9.99, 'main dish'),
('grapefruit', 2.99, 'dessert')
]

category = input("Enter appetizer, main dish, or dessert: ")

for item in menu:
    if item[2] == category:
        print(item[0], item[1])

print("part 2")
import re
from collections import defaultdict

def get_word_count(text):
    # convert the text to lowercase and split it into a list of words
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    
    # create a dictionary to store the frequency of each word
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1
    
    # return the list of tuples sorted by frequency
    return sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# open the text file and read its contents
with open('gettysburg.txt', 'r') as f:
    text = f.read()

word_count = get_word_count(text)

# print out the results
for word, count in word_count:
    print(f"{count} {word}")
