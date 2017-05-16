elements = [10,20,0,40,15] # This is a list of byte numbers
x=bytes(elements) #converts the list into bytes array
print(x[0])
for n in x:
	print(n)

y = bytearray(elements)
print('old:',y[0])
y[0]=88
print('new:',y[0])

