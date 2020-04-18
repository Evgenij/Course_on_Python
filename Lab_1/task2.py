FirstArray = [12, 47, 43, 32, 15]
SecondArray = [10, 25, 32, 46, 53]

def detection(array):
	result = "True"
	for i in range(1, len(array)):
		if (array[i - 1] >= array[i]):
			result = "False"
			break
	print(result)

detection(FirstArray)
detection(SecondArray)