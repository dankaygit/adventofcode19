import numpy as np

### import the data into an array of ints (because the entries will be indices)
data = np.genfromtxt('/Users/dannykun1/Documents/repositories/github/adventofcode19/data/day5.csv', delimiter=',', dtype=int)

### Parts 1&2 together


# Function to determine length of instruction
#
# Function to implement the operations
# 3 and 4 are easy, it's write and read (output)
# 1 and 2 now need to be implemented with extra decyphering
#
# Read in instruction


# More Ops for part 2. Need to increase the get_op options and 
# Add Ops functions
def get_op(opcode):
    ## Checks the last digit of the opcode to determine the type of operation
    # Returns the type of operation and number of params in respective instruction
    # Returns a tuple of two values 
    if opcode == 99:
        return (opcode, 0)
    code = opcode%10
    if code not in [1,2,3,4,5,6,7,8]: raise Exception("Opcode {} not recognized".format(code))
    if code in [1,2,7,8]:
        return (code, 4)
    elif code in [3,4]:
        return (code, 2)
    else:
        return (code, 3)

## Set instruction values according to parameters (for Opcode 1 and 2) 
def set_values(instruction):
    opcode = instruction[0]
    params = int(opcode/100)
    vals = instruction[1:]
    if params not in [0,1,10,11]: raise Exception("Unexpected params enpointered: {}".format(params))
    if params == 0:
        vals[0] = data[instruction[1]]
        vals[1] = data[instruction[2]]
    elif params == 1:
        vals[1] = data[instruction[2]]
    elif params == 10:
        vals[0] = data[instruction[1]]
    return (vals)

## Opcode 3: Input
def write(data, val, address):
    data[address] = val

## Opcode 4: Output
def read(data, instr):
    if instr[0] == 104:
        return (instr[1])
    else: return (data[instr[1]])

# Opcode 5: jump-if-true
def jump_if_true(instr, pointer, stps):
    if instr[1] == 0:
        return (pointer + stps)
    else:
        return (instr[2])

# Opcode 6: jump-if-false
def jump_if_false(instr, pointer, stps):
    if instr[1] != 0:
        return (pointer + stps)
    else:
        return (instr[2])

# Opcode 7: less-than
def less_than(instr):
    if instr[1]< instr[2]:
        return(1)
    else: 
        return (0)

# Opcode 8: equals
def equals(instr):
    if instr[1] == instr[2]:
        return(1)
    else: 
        return (0)

## main program

def run_comp(data, ID=1):
    pointer = 0
    opcode, steps = get_op(data[pointer])

    while (opcode!=99):
        print ("pointer =", pointer)
        instr = data[pointer:(pointer+steps)]
        if opcode not in [3, 4]:
            vals = set_values(instr)

        if opcode == 1:
            data[vals[2]] = vals[0] + vals[1]
        elif opcode == 2:
            data[vals[2]] = vals[0] * vals[1]
        elif opcode == 3:
            write(data, ID, instr[1])
        elif opcode == 4:
            print (read(data, instr))
        elif opcode == 5:
            pointer = jump_if_true(instr, pointer, steps)
        elif opcode == 6:
            pointer = jump_if_false(instr, pointer, steps)
        elif opcode == 7:
            data[instr[3]] = less_than(instr)
        else:
            data[instr[3]] = equals(instr)
        
        if opcode not in [5,6]:
            pointer += steps
        opcode, steps = get_op(data[pointer])

run_comp(data, ID=5)


