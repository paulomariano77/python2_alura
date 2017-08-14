#/usr/bin/python
# -*- coding: UTF-8 -*-
import math

class Profile(object):
    'Classe default for user profiles'

    def __init__(self, name, tel, organization):
        self.name = name
        self.tel = tel
        self.organization = organization

    
    def printall(self):
        print 'Name: %s, Tel: %s, Organization: %s' % (self.name, self.tel, self.organization)


class Date(object):
    'Print date'

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    
    def print_date(self):
        print "%s/%s/%s" % (self.day, self.month, self.year)


class Peaple(object):
    'Print IMC'

    def __init__(self, name, weight, height):
        self.name = name
        self.weight = float(weight)
        self.height = float(height)
    

    def print_imc(self):
        calc_imc = self.weight / math.pow(self.height, 2)
        print 'IMC of %s: %.2f' % (self.name, calc_imc)

