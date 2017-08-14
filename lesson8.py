#/usr/bin/python

# ----------------------------------------------------------------------------------------------------------------------
# Lesson 8 - Object Oriented Programming (REGEX)
# ----------------------------------------------------------------------------------------------------------------------

from models import Profile
from models import Date
from models import Peaple

profile1 = Profile('Flávio', 'Null', 'Caelum')

print profile1.name
print profile1.organization

profile2 = Profile('Paulo', 'Secret', 'Caelum')
print profile2.name
print profile2.organization

profile1.printall()
profile2.printall()

# nomed params
profile3 = Profile(name='Paulo', organization='Caelum', tel='2101420')
profile3.printall()

print type(profile3)
print profile3.__class__

date1 = Date(21,11,2007)
date1.print_date()

peaple1 = Peaple('Paulo', 105, 1.78)
peaple1.print_imc()