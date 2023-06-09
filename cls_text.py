import re
from collections import Counter


class TextFunctions:

    def __init__(self, text: str):
        self.text = text


    def longest_word(self):
        """выводит самое длинное слово, при уcловии что оно одно,
        если несколько то первое, можно вывести список всех."""

        self.only_words = re.sub(r'[.,"\'-?:!;]', '', self.text)

        print([word for word in self.only_words.split()
               if len(word) == max(map(lambda x: len(x), self.only_words.split()))][0])

    def often_word(self):
        """метод - выводит самое часто встречающееся слово"""
        print(sorted(Counter(self.only_words.split()).items(), key=lambda x: x[1], reverse=True)[0][0])


    def all_palindromes(self):
        """метод выводит все палиндромы через запятую."""
        print(', '.join(filter(lambda x: x.lower() == x[::-1].lower(), self.only_words.split())))

    def symbols_quantity(self):
        """метод выводит количество спецсимволов в тексте """
        print(len(self.text) - len(self.only_words))


# тестовые данные

data = 'Написаться Ссасс, принимающий: на входаааааааааааа ПотОп... Один метод, метод,  должен выводить.. "в", метод- самое длинное слово в'

a = TextFunctions(text=data)
a.longest_word()
a.all_palindromes()
a.symbols_quantity()
a.often_word()

print(TextFunctions.longest_word.__doc__)
print(TextFunctions.often_word.__doc__)
print(TextFunctions.symbols_quantity.__doc__)
print(TextFunctions.all_palindromes.__doc__)