group1 = [1,2,3,4,5] #take a list of elements
search = int(input('Enter the element you wish to search for'))

for element in group1:
	if search==element:
		print('element found in group1')
		break
else:
	print('Element Not found in group1') #This is the else suite

