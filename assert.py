#understanding assert statement
x = int(input('Enter a number greater than 0'))
try:
	assert x>0 #Exception may occur here
	print('you Entered: ',x)
except AssertionError:
	print("Wrong Input entered") #exception