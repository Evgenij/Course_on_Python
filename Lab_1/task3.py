from random import randint

numCard = ""

for i in range(16):
	numCard = numCard + str(randint(0,9))
print("Исходный номер карты: "+ numCard)

print('Зашифрованный номер карты: {} **** **** {}'.format(numCard[0:4], numCard[-4:len(numCard) + 1]))
