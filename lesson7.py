#/usr/bin/python

# ----------------------------------------------------------------------------------------------------------------------
# Lesson 7 - Regular Expressions (REGEX)
# ----------------------------------------------------------------------------------------------------------------------

import re

result = re.match('Py', 'Python')
print result.group()

result = re.match('py', 'Python')
print type(result)

result = re.match('[pP]y', 'Python')
print result.group()

# find all character starting from A-Z and a-z
result = re.match('[A-Za-z]y', 'Python')
print result.group()

# find all character
results = re.findall('[A-Za-z]y', 'Python or jython')
print results

results = re.findall('[A-Za-z]y[A-Za-z]+', 'Python, jython or Pypy')
print results

results = re.findall('\wy\w+', 'Python, jython or Pypy')
print results

results = re.findall('\wy\w+', 'Python3, jython2 or Pypy')
print results

results = re.findall('\wy\w+\d', 'Python3, jython2 or Pypy')
print results

results = re.findall('[A-Za-z]+\d?', 'Python3, jython2 or Pypy')
print results

results =  re.findall('[fF]\w+','Nico, Flavio, Fabiana and Romulo')
print results

results = re.findall(r'[fF]\w{6}','Nico, Flavio, Fabiana and Romulo')
print results

results = re.findall(r'[fF]\w{6,20}','Nico, Flavio, Fabiana and Romulo')
print results

result = re.findall(r'^#', '# comment starting with #')
print result

result = re.match(r'.*br$', 'http://alura.com.br')
print result.group()

result = re.findall(r'([JP]\w+)', 'Java, JavaScript and Python')
print result

result = re.findall(r'(\w+\d$)', 'rota66 88centavos Peer2Peer Python2')
print result

result = re.findall(r'(^\d\w+)', '88centavos Peer2Peer Python2 99taxi')
print result

result = re.findall(r'(\d\w+)', '88centavos Peer2Peer Python2 99taxi')
print result

result = re.findall(r'(\b\d\w+)', '88centavos Peer2Peer Python2 99taxi')
print result

regex_url = r'(.*/perfis/\d+/invite$)'
exists = re.match(regex_url, 'http://django.com/perfis/123/invite')
print exists is None

letters = ['B','R','A','Z','I','L']
country = '-'.join(letters)
print country

names = ['Fabio', 'Flavio','Nico']
names_connected = ''.join(names)
print names_connected