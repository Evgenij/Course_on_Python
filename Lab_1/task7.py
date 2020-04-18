address_list = [
	"www.Google",
	"https://www.youtube",
	"https://github.com/Evgenij",
	"www.pinterest.ru"
]
result_list = []

for string in address_list:
	tempString = string
	if string.startswith("www"):
		tempString = "http://"+string
	if not string.endswith(".com"):
		tempString = tempString + ".com"

	result_list.append(tempString)

print("Начальные адреса:"," | ".join(address_list))
print("Конечные адреса:"," | ".join(result_list))

