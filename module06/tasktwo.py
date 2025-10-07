"""
Task two, reading data from Excel and plotting turbine data on one figure
Initially read this to mean one plot but actually one figure can have subplots so have created both below
"""

import pandas as pd 
import matplotlib.pyplot as plt

#reading the data from Excel file
df = pd.read_excel('Assignments_46W38\module06\Module 6 - Exercises Data.xlsx', sheet_name = "Exercise 2")

#setting up x axis and all 4 series'
X = df['Wind speed (m/s)']
Y1 = df['Power (kW)']
Y2 = df['Thrust (kN)']
Y3 = df['Rotor speed (rpm)']
Y4 = df['Blade pitch (degrees)']



"""
Initial code for all in one plot:
fig, ax1 = plt.subplots()
#setting up the initial Y axis - not ideal to have Thrust on the same axis but assume only 2 axis are possible??
#tested with a 3rd axis but it overlaps and looks quite messy. Interesting to see how else it may be done
ax1.set_xlabel('Wind speed (m/s)')
ax1.set_ylabel('Power (kW) / Thrust (kN)')

ax1.plot(X,Y1, label = 'Power (kW)')
ax1.plot(X,Y2, label = 'Thrust (kN)')

ax2 = ax1.twinx()
ax2.set_ylabel('Rotor speed (rpm) / Blade pitch (degrees)')
ax2.plot(X,Y3, color = 'green',label = 'Rotor speed (rpm)')
ax2.plot(X,Y4, color = 'purple',label = 'Blade pitch (degrees)')
"""

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

ax1.plot(X,Y1)
ax1.set_xlabel('Wind speed (m/s)\n\n' + r'$\mathbf{(a)~Power}$')
ax1.set_ylabel('Power (kW)')
#ax1.set_title('Turbine Power')

ax2.plot(X,Y2)
ax2.set_xlabel('Wind speed (m/s)\n\n' + r'$\mathbf{(b)~Thrust}$')
ax2.set_ylabel('Thrust (kN)')
#ax2.set_title('Turbine Thrust')

ax3.plot(X,Y3)
ax3.set_xlabel('Wind speed (m/s)\n\n' + r'$\mathbf{(c)~Rotor~Speed}$')
ax3.set_ylabel('Rotor speed (rpm)')
#ax3.set_title('Turbine Rotor Speed')


ax4.plot(X,Y4)
ax4.set_xlabel('Wind speed (m/s)\n\n' + r'$\mathbf{(d)~Blade~Pitch}$')
ax4.set_ylabel('Blade pitch (degrees)')
#ax4.set_title('Turbine Blade Pitch')


fig.suptitle('Turbine Metrics')
fig.legend()
#fig.tight_layout()

fig.subplots_adjust(left=0.1, right=0.9,top=0.9,bottom = 0.2, wspace = 0.25, hspace = 0.6)

plt.show()


