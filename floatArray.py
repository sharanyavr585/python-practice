from array import *

arr1 = array('d',[1.5,2.0,5.9,3.3])

arr2 = array(arr1.typecode,(k for k in arr1))

for x in arr2:
	print(x)