import numpy as np
from itertools import permutations 

### import the data into an array of ints (because the entries will be indices)
data = np.genfromtxt('/Users/dannykun1/Documents/repositories/github/adventofcode19/data/day7.csv', delimiter=',', dtype=int)

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
def set_values(data, instruction):
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
def jump_if_true(vals, pointer, stps):
    if vals[0] == 0:
        return (pointer + stps)
    else:
        return (vals[1])

# Opcode 6: jump-if-false
def jump_if_false(vals, pointer, stps):
    if vals[0] != 0:
        return (pointer + stps)
    else:
        return (vals[1])

# Opcode 7: less-than
def less_than(vals):
    if vals[0]< vals[1]:
        return(1)
    else: 
        return (0)

# Opcode 8: equals
def equals(vals):
    if vals[0] == vals[1]:
        return(1)
    else: 
        return (0)

## main comp

def run_comp(data, inpt=1, phase=0, loop = False):
    local_data = np.copy(data)
    pointer = 0
    opcode, steps = get_op(local_data[pointer])
    if loop: outputs = []

    while (opcode!=99):
        instr = local_data[pointer:(pointer+steps)]
        print ("pointer =", pointer)
        print ("data chunk:", instr)
        if opcode not in [3, 4]:
            vals = set_values(local_data, instr)
            print ("Vals:", vals)

        if opcode == 1:
            local_data[vals[2]] = vals[0] + vals[1]
        elif opcode == 2:
            local_data[vals[2]] = vals[0] * vals[1]
        elif opcode == 3:
            if pointer == 0:
                write(local_data, phase, instr[1])
            else:
                write(local_data, inpt, instr[1])
        elif opcode == 4:
            output = read(local_data, instr)
            if loop: outputs.append(output)
            print (output)
        elif opcode == 5:
            pointer = jump_if_true(vals, pointer, steps)
        elif opcode == 6:
            pointer = jump_if_false(vals, pointer, steps)
        elif opcode == 7:
            local_data[instr[3]] = less_than(vals)
        else:
            local_data[instr[3]] = equals(vals)
        
        if opcode not in [5,6]:
            pointer += steps
        opcode, steps = get_op(local_data[pointer])
        print ("data[8]:", local_data[8])

    if not(loop): return (output)
    else: return (outputs)

### main program
# Part 1
phases = [0,1,2,3,4]
thruster_signals = []
perm_i = 0
permuts = np.array(list(permutations(np.array(phases))))
for perm in permuts:
    print ("Permutation #", perm_i," : ", perm)
    phases = list(perm)
    next_input = 0
    for phase in phases:
        inpt = next_input
        next_input = run_comp(data, inpt, phase)
    thruster_signals.append(next_input)
    perm_i += 1

solution = max(thruster_signals)

print (solution)

### main program
# Part 2

# phases = [i for i in range (5,10)]
# thruster_signals = []
# perm_i = 0
# permuts = np.array(list(permutations(np.array(phases))))


