import numpy as np

### import the data into an array of ints (because the entries will be indices)
data = np.genfromtxt('/Users/dannykun1/Documents/repositories/github/adventofcode19/data/day2.csv', delimiter=',', dtype=int)

### Part 1
def run_comp(data, inputs = np.array([12,2])):

    ### Initializations
    data[1:3] = inputs
    counter = 0
    current = data[counter:counter+4]
    op = current[0]

### Running the int computer
    while (op != 99):
        if op == 1:
            data[current[3]] = data[current[1]] + data[current[2]]
        if op == 2:
            data[current[3]] = data[current[1]] * data[current[2]]
        counter += 4
        current = data[counter:counter+4]
        op = current[0]
    return (data)

### print the solution
print (data[0])

### Part 2:
## Find 'inputs' i.e. data[1] and data[2] values,
## such that the exit value, data[0], equals 19690720
cycle = 0
for i in np.arange(100):
    for j in np.arange(100):
        print ("Cycle ", cycle, " of 10000")
        inputs = np.array([i,j])
        new_data = run_comp(data, inputs)
        if new_data[0] == 19690720: break
        cycle += 1

solution = 100 * new_data[1] + new_data[2]