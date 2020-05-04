
class StringFormatter:
	def __init__(self, str):
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
		return self.string.replace('',' ')[1:]

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



if __name__ == "__main__":
	string = StringFormatter("112some str3334ing f5or exa3455mple")
	print(string.delete_words(8))
	print(string.replacement())
	print(string.sort_lenght())
	print(string.insert_spaces())
	print(string.sort_lex())