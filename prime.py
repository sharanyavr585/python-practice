x = int(input('Enter the number until which you want to find the prime numbers'))
for i in range(2, x+1):
	for j in range(2,i):
		if(i%j==0):
			break;
	else:
		print(i)
			


