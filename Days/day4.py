import numpy as np
import collections

## Input to Day 4
pass_range = np.arange(372037, 905157+1)
pass_range_str = np.array(pass_range, dtype=str)

## Part 1

## The two functions needed to check the conditions for the passwords
## We don't check for the 1st condition (len == 6) because it's automatically met by the input
def repeat_check(number):
    i = 0
    double = False
    while(i<len(number)-1 and not(double)):
        double = number[i] == number[i+1]
        i += 1
    return (double)

def increase_check(number):
    i = 0
    increase = True
    while(i<len(number)-1 and increase):
        increase = number[i] <= number[i+1]
        i += 1
    return (increase)

repeated = np.array([number for number in map(repeat_check, pass_range_str)])
increased = np.array([number for number in map(increase_check, pass_range_str)])

solution = np.where(repeated & increased == True)[0]
print (len(solution))

## Part 2

## Input to Part 2 from Part 1
new_passes = pass_range_str[solution]

def absolute_doubles(number):
    uniques = list(set(number))
    counts = np.zeros(len(uniques))
    for i in np.arange(len(uniques)):
        for char in number:
            counts[i] += uniques[i] == char

    return ((counts == 2).any()==True)
    
sift = np.array([num for num in map(absolute_doubles, new_passes)])
sifted = new_passes[sift]

solution = len(sifted)
