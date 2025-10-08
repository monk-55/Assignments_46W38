"""
Module 6 task 3
Creating a 3d plot of Cp varying with blade pitch angle and the tip speed ratio
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#reading the data from Excel file
Turbine_Base = pd.read_excel('Assignments_46W38\module06\Module 6 - Exercises Data.xlsx', sheet_name = "Exercise 4 - Baseline")
Turbine_A = pd.read_excel('Assignments_46W38\module06\Module 6 - Exercises Data.xlsx', sheet_name = "Exercise 4 - A")
Turbine_B = pd.read_excel('Assignments_46W38\module06\Module 6 - Exercises Data.xlsx', sheet_name = "Exercise 4 - B")

Rotor_speed_Base = Turbine_Base['Rotor speed (rpm)']
Rotor_speed_A = Turbine_A['Rotor speed (rpm)']
Rotor_speed_B = Turbine_B['Rotor speed (rpm)']


"""
#Code below is for part 1

X=Turbine_Base['Time (s)']

fig, ax = plt.subplots()
ax.plot(X, Rotor_speed_Base, label = 'Baseline')
ax.plot(X, Rotor_speed_A, label = 'A')
ax.plot(X, Rotor_speed_B, label = 'B')
ax.set_xlabel("Time (s)")
ax.set_ylabel("Rotor Speed (rpm)")
ax.legend()
#ax.set_title("Rotor speeds of 3 turbines")
plt.show()
"""
######################################
"""
Part 2 - calculate standard deviation of each metric and plot these, normalise against baseline
Blade Pitch, rotor speed, platform pitch, Thrust, Tower base moment
"""

#Calculate SDs per turbine
Base_SD = Turbine_Base.std()
df_Base_SD = pd.DataFrame(Base_SD, columns=['SD'])
A_SD = Turbine_A.std()
df_A_SD = pd.DataFrame(A_SD, columns=['SD'])
B_SD = Turbine_B.std()
df_B_SD = pd.DataFrame(A_SD, columns=['SD'])

"""X = df_A_SD.index
Y1 = df_Base_SD['SD']
Y2 = df_A_SD['SD']
Y3 = df_B_SD['SD']

fig, ax = plt.subplots()
ax.plot(X, Y1, label = 'Baseline')
ax.plot(X, Y2, label = 'A')
ax.plot(X, Y3, label = 'B')

plt.show()
"""

#calculate normalised data as numpy arrays
Norm_Base = np.array(Base_SD / Base_SD)
Norm_A = np.array(A_SD / Base_SD)
Norm_B = np.array(B_SD / Base_SD)

#easiest way to define X series was to pull it from a dataframe as per the examples
X = df_Base_SD.index
#Y series are numpy arrays
Y1 = Norm_Base
Y2 = Norm_A
Y3 = Norm_B

fig, ax = plt.subplots()
ax.plot(X, Y1, label = 'Baseline')
ax.plot(X, Y2, label = 'A')
ax.plot(X, Y3, label = 'B')
ax.legend()

plt.show()

