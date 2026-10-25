import numpy as np
import parse as ps
import matplotlib.pyplot as plt
from scipy.integrate import odeint # Import the necesary libraries and functions

beta =1.0/1000 # How quickly infections occur, the number of infections per person per hour
gamma =1.0/(24*14) # (=1.0/336 per hr)The recovery rate constant per hour with a mean infectious period of 14 days
beta = beta * 168  # How quickly infections occur per person per week (1/1000pers/hrs * 168hrs/week)
gamma = gamma * 168 # The recovery rate per week (1/(24*14)recovery/hrs * 168hrs/week)
gamma = 1.25 # How quickly infections occur per person per week
beta = 1.8e-5 # The recovery rate per week

s = ps.s
def deriv (x,t):
	ifc = beta *x [0]* x [1]  # Infection rate, susecptible people move from S to I
	rec = gamma *x [1] # Recovery rate, infected people move from I to R
	return np.array([-ifc ,ifc -rec, rec]) 
# Resulting rates of change dS/dt=-BSI, dI/dt=BSI-YI, dR/dt=YI respectively

# Create an array of 1000 points equally spaced in 0-12weeks that represents the times at which to 
# calculate the solution. (2000hrs / 168hrs/week \approx 12weeks)
time = np.linspace(0, 50, 1000)
xinit =np.array ([108600, 25 ,0]) # Initial values of the three variables S(0), I(0), R(0) respectively
x= odeint(deriv, xinit, time ) # Compute the solution to the differential equation dS/dt, dI/dt, dR/dt
plt.figure() # Create a new figure
plt.plot(s[1][1:52], '-', label="data")
# p0 ,= plt.plot (time ,x [: ,0]) # Plot the value of the "succeptible" population at each time
p1 ,= plt.plot (time ,x [: ,1], label="I(t)") # Plot the value of the "infected" population at each time
# p2 ,= plt.plot (time ,x [: ,2]) # Plot the value of the "removed" population at each time
# plt.legend([p0 ,p1 ,p2 ],["S(t)","I(t)","R(t)"]) # Label each plot and create legend
plt.xlabel('t ( Weeks )') # Label the x-axis as time in weeks
plt.ylabel('Population') # Label the y-axis as population
plt.legend()
plt.show() # Show the figure

# time =np.linspace (0,12,1000)  


