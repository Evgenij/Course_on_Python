
listSymbols = []
text = "Some text"
# result = S,o,m,x

for index in range(len(text)):
	tempSymbol = text[int(index)]
	#print(tempSymbol)
	countSymbols = 0

	for symbol in text:
		if symbol == tempSymbol and symbol != ' ':
			countSymbols += 1
		else:
			continue

	if countSymbols == 1:
		listSymbols.append(tempSymbol)
	else:
		continue


print("Символы, которые встречаются 1 раз:",",".join(listSymbols))