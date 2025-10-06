"""
module06 task 1
"""

import matplotlib.pyplot as plt

X = ['Crude oil', 'Natural gas', 'Renewable energy', 'Solid fuels', 'Nuclear Energy']
Y = [37.7, 20.4, 19.5, 10.6, 11.8]

fig, ax = plt.subplots()

ax.set_xlabel('Energy source')
ax.set_ylabel('Percentage of total energy generation (%)')

ax.set_title('Percentage shares of energy generation within the EU in 2023')

ax.bar(X,Y, color='blue')
plt.show()