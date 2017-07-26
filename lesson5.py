# ----------------------------------------------------------------------------------------------------------------------
# Lesson 5 - Recording profiles
# ----------------------------------------------------------------------------------------------------------------------

from sys import stdout
from datetime import date

def register(names):
    name = raw_input('Input your name: ')
    names.append(name)

def calc_age(birthday_year):
    actualy_year = date.today().year
    return actualy_year - int(birthday_year)

def remove_names(names):
    name = raw_input('What name would you like to remove?\n')
    names.remove(name)
    return names

if __name__ == '__main__':
    names = []
    for i in range(0,4):
        register(names)

    for name in names:
       stdout.write(name + " ")

    birthday_year = raw_input('\nInput your birthday year: ')
    print 'Your age is %s' % (calc_age(birthday_year))

    remove_names(names)
    print 'Your new name is: '
    for name in names:
       stdout.write(name + " ")