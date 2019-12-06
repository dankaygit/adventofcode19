import numpy as np
import matplotlib.pyplot as plt
from itertools import product

### import the data into an array of ints (because the entries will be indices)
input_data = np.genfromtxt('/Users/dannykun1/Documents/repositories/github/adventofcode19/data/day3.csv', delimiter=',', dtype=str)

### Part 1

# First try ####
# Using 2D arrays and comparing, not smart...

# ## Record every position that's passed by both lines 
# ## then compare them
pos1 = np.zeros((1,2), dtype=int)
pos2 = np.zeros((1,2), dtype=int)

# ## Let's define the starting point as the origin (0,0)

def move(str, last_pos):
    direction = str[0]
    steps = int(str[1:])

    pos = np.full((steps, 2), last_pos)

    if direction=='R':
        pos[:,0] += np.arange(1,steps+1)
    elif direction=='L':
        pos[:,0] -= np.arange(1,steps+1)
    elif direction=='U':
        pos[:,1] += np.arange(1,steps+1)
    elif direction=='D':
        pos[:,1] -= np.arange(1,steps+1)
    
    return (pos)

for str in input_data[0]:
    pos1 = np.vstack((pos1, move(str, pos1[-1])))
for str in input_data[1]:
    pos2 = np.vstack((pos2, move(str, pos2[-1])))

plt.figure()
plt.xlim(-280, -270)
plt.ylim(-1070, -1065)
plt.plot(pos1[:10000,0], pos1[:10000,1], 'g-')
plt.plot(pos2[:10000,0], pos2[:10000,1], 'r-')
plt.grid(True)
plt.Circle((0,0), radius = 1000)
plt.savefig("paths.eps")

### Saw that solution must be near those values:
### Found value [-277, -1068]

steps1 = int(np.where((pos1==[-277, -1068]).all(1))[0])
steps2 = int(np.where((pos2==[-277, -1068]).all(1))[0])

solution = steps1 + steps2 

# equals = np.where((pos1==pos2[:,None]).all(-1))[1]

# End of First Try ####

# Second Try ####
# Use 1D arrays of tuples

    ### Initializations

### print the solution


### Part 2:
## Find 'inputs' i.e. data[1] and data[2] values,
## such that the exit value, data[0], equals 19690720


