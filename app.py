# ----------------------------------------------------------------------------------------------------------------------
# Lesson 6 - Organizing our code better
# ----------------------------------------------------------------------------------------------------------------------
# -*- coding: UTF-8 -*-

from sys import stdout
import re


def register(names):
    name = raw_input('\nInput your name: ')
    names.append(name)


def to_list(names):
    print '\nListing names: '
    for name in names:
        print name


def remove_names(names):
    name = raw_input('\nWhat name would you like to remove?\n')
    names.remove(name)
    return names


def update_names(names):
    name = raw_input('\nWhat name would you like to edit?')
    if (search(name, names)):
        index = names.index(name)
        new_name = raw_input('Type it a new name: ')
        names[index] = new_name


def search(name, names):
    if (name in names):
        print 'Name %s finded' % (name)
        return True
    else:
        print "Name %s don't finded" % (name)


def find_regex(names):
    print 'Enter a regex expression'
    regex = raw_input()
    names_connected = ''.join(names)
    find = re.findall(regex, names_connected)
    print find


def menu():
    names = []
    option = 0
    while (option != 5):
        print '\nType it: 0 to register, 1 to list, 2 to remove, 3 to update name or, 4 to find, 5 to exit'
        option = int(raw_input())

        if (option == 0):
            register(names)

        if (option == 1):
            to_list(names)

        if (option == 2):
            if (len(remove_names(names)) > 0):
                print 'Your new name is: '
                for name in names:
                    stdout.write(name + " ")
            else:
                print 'No search elements'

        if (option == 3):
            update_names(names)
        
        if (option == 4):
            find_regex(names)


menu()
