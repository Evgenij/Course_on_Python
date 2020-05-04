
class StringFormatter:
	def set_string(self, str):
		self.string = str

	# удаление всех слов из строки, длина которых меньше n букв
	def delete_words(self, n):
		words = self.string.split(' ')
		self.string = ' '.join(list(filter(lambda word: len(word) >= n, words)))
		return self.string

	# замена всех цифр в строке на знак «*»
	def replacement(self):
		for symbol in self.string:
			if str(symbol).isdigit():
				self.string = self.string.replace(symbol,'*')
		return self.string

	# вставка по одному пробелу между всеми символами в строке
	def insert_spaces(self):
		self.string = self.string.replace('',' ')[1:]

	# сортировка слов по размеру
	def sort_lenght(self):
		self.string = self.string.split()
		self.string.sort(key=len)
		self.string = ' '.join(self.string)
		return self.string

	# сортировка слов в лексикографическом порядке
	def sort_lex(self):
		self.string = ' '.join(sorted(self.string.split(' ')))
		return self.string

	def formatting(self,
	                delete = False, n = 0,
	                replace = False,
	                spaces = False,
	                sort_lenght = False,
	                sort_lex = False):
		if delete == True:
			if n != 0:
				self.delete_words(n)
		if replace == True:
			self.replacement()
		if spaces == True:
			self.insert_spaces()
		if sort_lenght == True:
			self.sort_lenght()
		if sort_lex == True:
			self.sort_lex()

		return self.string