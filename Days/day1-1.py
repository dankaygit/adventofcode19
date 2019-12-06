import numpy as np

#import the data into an array
data = np.genfromtxt('/Users/dannykun1/Documents/repositories/github/adventofcode19/data/day1.csv', delimiter=',')
fuel = 0
pos = np.arange(len(data))

#make the compution from day 1 part 2
while(data.sum()>0):
    data[pos] = data[pos]//3 - 2
    pos = data>0
    data[np.logical_not(pos)] = 0
    fuel += data.sum()
    print (data)
    print (fuel)


#print the solution
print (fuel)