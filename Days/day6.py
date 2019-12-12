import numpy as np
import pandas as pd

orbit_data = pd.read_csv('/Users/dannykun1/Documents/repositories/github/adventofcode19/data/day6.csv', names = ['raw'])
orbit_strings = orbit_data['raw']
orbit_data['centers'] = orbit_strings.str.extract('(.*?)\)')
orbit_data['orbiting'] = orbit_strings.str.extract('\)(.*)')

orbits = pd.concat([orbit_data['centers'], orbit_data['orbiting']], ignore_index=True).unique()


families = orbit_data['orbiting'].value_counts().to_frame()
families['level'] = np.zeros(families.shape[0], dtype=int)

def find_level(child, orbit_data=orbit_data):
    level = 0
    while(child != 'COM'):
        child = orbit_data['centers'][orbit_data['orbiting'] == child].iloc[0]
        level+=1
    return (level)

for i in np.arange(families.shape[0]):
    print (i)
    families['level'][i] = find_level(orbit_data['orbiting'][i])

print (families['level'].sum())

def get_path(child, orbit_data=orbit_data):
    path = [child]
    while(child != 'COM'):
        child = orbit_data['centers'][orbit_data['orbiting'] == child].iloc[0]
        path.append(child)
    return (np.array(path))

you_path = get_path('YOU')
san_path = get_path('SAN')

def find_node(path1, path2):
    i = 1
    while(path1[-(i+1):-i]==path2[-(i+1):-i]):
        i+=1
    print(i)
    return(path1[-i:-(i-1)])

node = find_node(you_path, san_path)
hops = np.where(you_path==node)[0][0] - 1 + np.where(san_path==node)[0][0] - 1



