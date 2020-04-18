
#35500
Banknotes = {
	"5000": 3,
	"1000": 8,
	"500": 10,
	"100": 14,
	"50": 100,
	"10": 100,
	"1": 100
}

money = int(input("Введите сумму:"))

#подсчет денег в банкомате
moneyBanknotes = 0
for key in Banknotes.keys():
	moneyBanknotes = moneyBanknotes + int(key)*Banknotes[key]

if money > moneyBanknotes:
	print("Недостаточно средств в банкомате...")
else:
	get = { }
	for key in Banknotes.keys():
		countBanknote = 0 #кол-во купюр
		while (money >= int(key)) and (Banknotes[key] > 0):
			money -= int(key)
			countBanknote += 1
			Banknotes[key] = Banknotes[key] - 1
		get[key] = countBanknote

	getBanknotes = 0
	for key in get.keys():
		getBanknotes = getBanknotes + int(key) * get[key]

	if money > getBanknotes:
		print('Операция не может быть выполнена!')
	else:
		print('+'.join([("%s*%s" % (key, get[key])) for key in get.keys() if (get[key] != 0)]))
