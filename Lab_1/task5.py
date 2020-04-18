startString = str(input("Введите предолежние: "))
finallyString = startString

tempString = startString.split(' ')
for word in tempString:
	if str(word).istitle():
		finallyString = str(finallyString).replace(word, str(word).upper())

print(finallyString)