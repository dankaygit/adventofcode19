import numpy as np
import pandas as pd

orbit_data = pd.read_csv('/Users/dannykun1/Documents/repositories/github/adventofcode19/data/day6.csv', names = ['raw'])
orbit_strings = orbit_data['raw']
orbit_data['centers'] = orbit_strings.str.extract('(.*?)\)')
orbit_data['orbiting'] = orbit_strings.str.extract('\)(.*)')

orbits = pd.concat([orbit_data['centers'], orbit_data['orbiting']], ignore_index=True).unique()

orbit_data['centers'].

families = pd.DataFrame({'objects': orbits})
families['level'] = np.zeros(families.shape[0])

levels = {
    'COM' : 0
}

next = orbit_data['orbiting'][orbit_data['centers']]