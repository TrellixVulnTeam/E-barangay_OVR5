def FibxFac(n):
	first = 0
	second = 1
	temp = 0
	factrial = 1
	for i in range(0,n+1):
		temp = first + second
		print(temp)
		factrial = factrial * temp
		first = second
		second = temp
	print("The Fibbonacci Factorial is: "+str(factrial))
FibxFac(5)