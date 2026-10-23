import matplotlib.pyplot as plt
import numpy as np

# Open the file in the "read" mode
f=open("googleflu.csv","r")

# Read in header line
h=f.readline().split(",")

# Initialize 53 empty lists
s=[]
for i in range(53):
	s.append([])

# Loop over the remaining lines
for l in f:

    # Create a list by separating the line at commas
    d=l.split(",")
    for i, val in enumerate(d):
      if val=='' or val.isspace():
        d[i] = np.nan #type: ignore

    # Store the 53 entries in the line to each relevant list
    for i in range(53):
      if i==0:
        s[i].append((d[i]))
      else:
        s[i].append(float(d[i]))

# Close the file
f.close()

plt.figure()
p3,=plt.plot(s[1][1:52],"-")
plt.legend([p3],["Data", "I(t)"])
plt.xlabel("t (Weeks)")
plt.ylabel("Population")
plt.show()