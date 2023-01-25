import matplotlib.pyplot as plt

# Data for population in various European countries
data = {'France': 65, 'England': 68, 'Belgium': 12, 'Germany': 84, 'Austria': 9, 'Switzerland': 9}

# Pie chart
plt.pie(data.values(), labels=data.keys(), explode=[0, 0, 0.1, 0, 0, 0.1], autopct='%1.1f%%')
plt.title("Population in European Countries (Q1)")
plt.legend(title="Countries")

# Save the resulting graph
plt.savefig("European_population(Q1).png")

plt.figure(figsize=(5, 2.5))
plt.bar(data.keys(), data.values())
plt.xlabel("Countries")
plt.ylabel("Population (in millions)")
plt.title("Population in European Countries (Q2)")
plt.subplots_adjust(bottom=0.3)

# Save the resulting graph
plt.savefig("European_population(Q2).png")


# Horizontal bar chart
plt.figure(figsize=(10, 5))
plt.barh(list(data.keys()), list(data.values()))
plt.ylabel("Countries (horizontal)")
plt.xlabel("Population (in millions)")
plt.title("Population in European Countries (Q3)")

plt.subplots_adjust(left=0.3)

# Save the resulting graph
plt.savefig("European_population(Q3).png")


import matplotlib.pyplot as plt

# Data for IQ of men and women as a function of age
ages = [5, 10, 15, 20, 25]
men_iq = [65, 70, 90, 110, 125]
women_iq = [70, 80, 100, 105, 115]

# Line graph
plt.figure(figsize=(10, 5))
plt.plot(ages, men_iq, '-o', label='Men')
plt.plot(ages, women_iq, '-o', label='Women')
plt.xlabel("Age (years)")
plt.ylabel("IQ")
plt.title("IQ as a function of age for men and women (Q4)")
plt.legend()

# Save the resulting graph
plt.savefig("IQ_men_women(Q4).png")


# Show the graph
plt.show()
