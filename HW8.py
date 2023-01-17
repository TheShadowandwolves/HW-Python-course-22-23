import numpy as np

fruit = np.array(['apricots', 'bananas', 'cherries', 'melon', 'oranges', 'strawberries'])
cost = np.array([35, 22, 50, 25, 15, 40])

# 1a. The price of each item increases by  2 shekel.
cost = cost + 2
print("part 1a\n" + str(cost))
# 1b. The price of each item is increased by 20%.
cost = cost * 1.2
print("part 1b\n" + str(cost))
# 1c. The following items are increased by the following amounts: strawberries: 5,  cherries: -3, apricots: 4.
cost[fruit == 'strawberries'] += 5
cost[fruit == 'cherries'] -= 3
cost[fruit == 'apricots'] += 4

# 1d. If all 3 changes are applied, one after the other, what will the final prices be?
print("part 1d\n" + str(cost))

# 2. 
cherries_bill = cost[fruit == 'cherries'] * 30
strawberries_bill = cost[fruit == 'strawberries'] * 15
melon_bill = cost[fruit == 'melon'] * 40
bananas_bill = cost[fruit == 'bananas'] * 55
apricots_bill = cost[fruit == 'apricots'] * 80

total_bill = cherries_bill + strawberries_bill + melon_bill + bananas_bill + apricots_bill
print(total_bill)

#3a
sunday_sales = ['s','m','s','o','o','b','a','b','o','m','b','b','m','s','o','o','m','s','b','o','o','b','o','s','o','a','b','a','a','b','m','m','a','b']

unique, counts = np.unique(sunday_sales, return_counts=True)

frequency_table = dict(zip(unique, counts))
print(frequency_table)

#3b
# Sample data
data = sunday_sales
# Count the frequency of each fruit
fruit_count = {}
for fruit in data:
    if fruit not in fruit_count:
        fruit_count[fruit] = 0
    fruit_count[fruit] += 1

#total sales of sunday
total_kg_sunday = sum(fruit_count.values())

# Calculate relative frequency
relative_frequency = {}
for fruit, count in fruit_count.items():
    relative_frequency[fruit] = round((count / total_kg_sunday) * 100, 2)

# total order of sunday
total_kg_order_sunday = {}
for fruit, rel_freq in relative_frequency.items():
    total_kg_order_sunday[fruit] = round((rel_freq/100)*(1.75*total_kg_sunday),2)

# Print the total order on sunday
for fruit, count in total_kg_order_sunday.items():
    print(f"{fruit} : {count}")

# Print the relative frequency table
print("| Fruit | Frequency | Relative Frequency (%) |")
print("|-------|-----------|------------------------|")
for fruit, rel_freq in relative_frequency.items():
    print(f"| {fruit}     | {fruit_count[fruit]}        | {rel_freq}                     |")

#3c.
Mondayssales = total_kg_sunday * -0.1
Tuesday = total_kg_sunday
Wednesday = total_kg_sunday *  (0.1)
Thursday = total_kg_sunday * (0.3)
Friday = total_kg_sunday * (0.25)

total_sale = Mondayssales + Tuesday + Wednesday + Thursday + Friday
print("Monday: " + str(Mondayssales))
print("Tuesday" + str(Tuesday))
print("Wednesday" + str(Wednesday))
print("Thursday" + str(Thursday))
print("Friday" + str(Friday))

#3d.
#total order
print("total order: " + str(total_sale))

#3e.
newcost = cost * 0.8
print("part 3e\n" + str(newcost))

#3f.
tt = Wednesday + Friday + total_kg_sunday
print("part 3f\n " + str(tt))

#3g.
print("part 3g\n" + str(Wednesday))

#3h.
print("part 3h\n" + str(Wednesday * 0.72) )

#3i.
print("part 3i:")
# New items to add
new_fruit = ["blueberries", "raspberries", "plums"]
new_cost = [45, 70, 30]

# Zip into list of tuples
fruit_cost_tuples = list(zip(fruit, cost))
new_tuples = list(zip(new_fruit, new_cost))

# Extend and sort the list
fruit_cost_tuples.extend(new_tuples)
fruit_cost_tuples.sort()

# Print out columns of fruits and costs
for item in fruit_cost_tuples:
    print(item[0], "\t", item[1])