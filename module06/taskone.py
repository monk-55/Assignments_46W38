"""
module06 task 1
First plot simple bar chart
Second plot pie chart
"""

import matplotlib.pyplot as plt

X = ['Crude oil', 'Natural gas', 'Renewable energy', 'Solid fuels', 'Nuclear Energy']
Y = [37.7, 20.4, 19.5, 10.6, 11.8]

fig, ax = plt.subplots()

"""
code commented out is for a bar chart
"""
# ax.set_xlabel('Energy source')
# ax.set_ylabel('Percentage of total energy generation (%)')

# ax.set_title('Percentage shares of energy generation within the EU in 2023')

# ax.bar(X,Y, color='blue')


""" the code line below is specific for a pie chart
plt.show() is used for both examples"""
wedges, texts, autotexts = ax.pie(Y, labels=X, autopct='%1.1f%%', startangle=90) 

plt.show()