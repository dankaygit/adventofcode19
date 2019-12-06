import numpy as np

### import the data into an array of ints (because the entries will be indices)
data = np.genfromtxt('/Users/dannykun1/Documents/repositories/github/adventofcode19/data/day5.csv', delimiter=',', dtype=int)

### Part 1


# Function to determine length of instruction
#
# Function to implement the operations
# 3 and 4 are easy, it's write and read (output)
# 1 and 2 now need to be implemented with extra decyphering
#
# Read in instruction


def get_op(opcode):
    ## Checks the last digit of the opcode to determine the type of operation
    # Returns the type of operation and number of params in respective instruction
    # Returns a tuple of two values 
    if opcode == 99:
        return (opcode, 0)
    code = opcode%10
    if code not in [1,2,3,4]: raise Exception("Opcode {} not recognized".format(code))
    if code < 3:
        return (code, 4)
    else:
        return (code, 2)

def read(data, instr):
    if instr[0] == 104:
        return (instr[1])
    else: return (data[instr[1]])

def write(data, val, address):
    data[address] = val

def set_values(instruction):
    opcode = instruction[0]
    params = int(opcode/100)
    vals = instruction[1:4]
    if params == 0:
        return (vals)
    else:
        if params%10 == 0:
            vals[0] = data[instruction[1]]
        params = int(params/10)
        if params%10 == 0:
            vals[1] = data[instruction[2]]
        return (vals)

## main program

def run_comp(data, ID=1):
    counter = 0
    opcode, steps = get_op(data[counter])

    while (opcode!=99):
        print ("Counter =", counter)
        instr = data[counter:(counter+steps)]

        if opcode == 1:
            vals = set_values(instr)
            data[vals[2]] = vals[0] + vals[1]
        elif opcode == 2:
            vals = set_values(instr)
            data[vals[2]] = vals[0] * vals[1]
        elif opcode == 3:
            write(data, ID, instr[1])
        else:
            print (read(data, instr))
        
        counter += steps
        opcode, steps = get_op(data[counter])

run_comp(data)


### Part 2:
## Find 'inputs' i.e. data[1] and data[2] values,
## such that the exit value, data[0], equals 19690720
# cycle = 0
# for i in np.arange(100):
#     for j in np.arange(100):
#         print ("Cycle ", cycle, " of 10000")
#         inputs = np.array([i,j])
#         new_data = run_comp(data, inputs)
#         if new_data[0] == 19690720: break
#         cycle += 1

# solution = 100 * new_data[1] + new_data[2]