from array import *

arr = array('i',[1,2,3,4,5])

n = len(arr)

i=0
while(i<n):
	print(arr[i])
	i=i+1

y = arr[1:4]
print(y)

print('------------')

k = arr[0:]
print(k)

print('------------')

m = arr[:4]
print(m)

print('------------')

l = arr[-4:]
print(l)

print('------------')

j = arr[-4:-1] # -4-(x)=-3
print(j)

print('------------')

d = arr[0:4:2]
print(d)

print('------------')

for t in arr[2:4]:
	print(t)







