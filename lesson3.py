# ----------------------------------------------------------------------------------------------------------------------
# Lesson 3 - Creating tuples and dictionarys in Python
# ----------------------------------------------------------------------------------------------------------------------
invite_types = ['vip', 'normal', 'half', 'cortesy']
print('invite types list', invite_types)

# Creating tuples
invite_types = ('vip', 'normal', 'half', 'cortesy')
print('invite types tuples', invite_types)
print('insite types in the positon 1', invite_types[1])

# Creating dictionary
invites_with_value = {invite_types[0] : 60, invite_types[1] : 40, invite_types[2] : 30, invite_types[3] : 0}
print(invites_with_value)
print('This value is', invites_with_value['vip'])
print('Print keys', invites_with_value.keys())
print('Print values', invites_with_value.values())

# Concatenating tuples
merital_status = ('married', 'single') + ('divorced',) # attention, you must have the comma after 'divorced'
print(merital_status)
print(type(merital_status))

# Converting lists in tuples
states = ('RJ', 'SP') + tuple(['MG', 'ES'])
print(states)
print(type(states))

# Returning max values of a tuple or list
print(max([10, 5, 7]))

# Returning min values of tuples or list
print(min([10, 3, 9]))

# Ordering lists or tuples
names = ('Leandro', 'Flavio', 'Romulo')
print(names)
print(sorted(names))
names = sorted(names)
print(names)