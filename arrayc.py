from array import *

a = array('u',['a','b','c','d'])

print('following are the charecters:')

for x in a:
	print(x)

b = array(a.typecode, (x for x in a))

print('following charecers have been put in b:')

for y in b:
	print(y)

