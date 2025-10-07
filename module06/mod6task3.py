"""
Module 6 task 3
Creating a 3d plot of Cp varying with blade pitch angle and the tip speed ratio
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#reading the data from Excel file
df = pd.read_excel('Assignments_46W38\module06\Module 6 - Exercises Data.xlsx', sheet_name = "Exercise 3", index_col = 0)

#assigning the tip speed ratios  and pitch angles (TSRs)
TSR = df.index.values.astype(float)
Pitch = df.columns.values.astype(float)
X, Y = np.meshgrid(Pitch, TSR)
Cp = df.values.astype(float)


fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('Pitch')
ax.set_ylabel('TSR')
ax.set_zlabel('Cp')

surf = ax.plot_surface(X, Y, Cp, cmap='inferno', edgecolor='none')

# Change the view
ax.view_init(elev=25, azim=125)

# Customize grid appearance
ax.xaxis._axinfo['grid']['color'] = 'lightgray'
ax.xaxis._axinfo['grid']['linestyle'] = '--'

ax.yaxis._axinfo['grid']['color'] = 'lightgray'
ax.yaxis._axinfo['grid']['linestyle'] = '--'

ax.zaxis._axinfo['grid']['color'] = 'lightgray'
ax.zaxis._axinfo['grid']['linestyle'] = '--'

# Add a color bar
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, pad=0.09)

plt.show()

