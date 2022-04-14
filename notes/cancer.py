#!usr/bin/env python3

table = {'EVENT': ['A', 'A0'],
         'PRIOR': [.001, .999],
         'COND': [.99, .02],
         'JOINT': [None, None],
         'POST': [None, None]}

# Joint 
for x, (y, z) in enumerate(zip(table['PRIOR'], table['COND'])):
    table['JOINT'][x] = y * z

# Posterior
total = sum(table['JOINT'])
for x, y in enumerate(table['JOINT']):
    table['POST'][x] = round(y / total, 5)

# Output
for key, value in table.items():
    print(f'{key:5} :', value)
