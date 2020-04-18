def print_format_text(resText):

	print("\n---- Длиннее 7 ----")
	for i in resText:
		if len(i) >= 7:
			print(i)

	print("\n---- Длиннее 5, но короче 7 ----")
	for i in resText:
		if len(i) >= 5 and len(i) < 7:
			print(i)

	print("\n---- Короче 5 ----")
	for i in resText:
		if len(i) < 5:
			print(i)


text = "Инвестиции являются неотъемлемой частью современной экономики. " \
       "От кредитов инвестиции отличаются степенью риска для инвестора (кредитора) - " \
       "кредит и проценты необходимо возвращать в оговорённые сроки независимо " \
       "от прибыльности проекта, инвестиции (инвестированный капитал) возвращаются " \
       "и приносят доход только в прибыльных проектах."

spaces = 0
for i in text:
	if i == ' ':
		spaces += 1

print(text)

resText = text.split(' ', spaces+1)

print_format_text(resText)

