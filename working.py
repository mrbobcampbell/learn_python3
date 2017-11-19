"""more_stuff = [1, 2, 3, 4, 5]

print(more_stuff.pop())
print(more_stuff.pop(0))
print(more_stuff)
more_stuff.insert(1, 99)
print(more_stuff)
more_stuff.sort()
print(more_stuff)

print(more_stuff.items())
"""

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print('-' * 10)
for i, x in states.items():
    print(f"{i} is abbreviated {x}")
