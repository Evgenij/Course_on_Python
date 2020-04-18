
def definition_complexity(password):
	countsPassword = 0

	if str(password).isdigit():
		print("Пароль не может состоять только из цифр.")
	else:
		countsPassword += len(password)
		for symbol in password:
			if str(symbol).isdigit():
				countsPassword += 1
			if str(symbol).isupper():
				countsPassword += 1
			if symbol == "_" or symbol == "." or symbol == "!":
				countsPassword += 1

		print("Сложность пароля:")
		if countsPassword < 6:
			print("[:||-------------:]")
		elif countsPassword < 10:
			print("[:||||-----------:]")
		elif countsPassword < 15:
			print("[:||||||---------:]")
		elif countsPassword < 20:
			print("[:|||||||||------:]")
		elif countsPassword < 25:
			print("[:||||||||||||---:]")
		else:
			print("[-|||||||||||||||-]")

#----------------------

password = input("Введите пароль: ")

while len(password) < 5:
	print("Пароль слишком короткий.")
	password = input("Введите пароль: ")

definition_complexity(password)