# ----------------------------------------------------------------------------------------------------------------------
# Lesson 2 - Creating lists in Python
# ----------------------------------------------------------------------------------------------------------------------
invite1 = 'Flavio Almeida'
invite2 = 'Nico Steappat'
invite3 = 'Romulo Henrique'

invites = [invite1, invite2, invite3]

# Print elemets list
print(invites)
print('Invites in the position 1', invites[1])
print('Invites in the position 2', invites[2])
print(invites[0:2])
print(invites[1:])

# Adding new elements
invites.append('Paulo Mariano')
print(invites)
invites.append(10)
print(invites)

# Removing elements
invites.remove(10)
print(invites)
invites.remove('Paulo Mariano')
print(invites)