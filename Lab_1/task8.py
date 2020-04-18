import random
import array

def countZero(number):
	for degree in range(1,15):
		if number > 2**(degree-1) and number < 2**(degree+1):
			return (2**(degree+1))-number


n = random.randint(1,10000)

arr = array.array("i",[])
for elem in range(n):
	rndNumber = random.randint(1,100)
	arr.append(rndNumber)

print("Длинна заполненного массива: " + str(len(arr)))
print("Кол-во добавляемых нулей: " + str(countZero(n)))

for elem in range(countZero(n)):
	arr.append(0)

print("Длинна конечного массива: " + str(len(arr)))


