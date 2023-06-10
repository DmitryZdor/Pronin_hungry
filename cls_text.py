import re
from collections import Counter

class TextFunctions:

    def __init__(self, text: str):
        self.text = text
        self.symbols = '.,"\'-?:!;$()'
        self.only_words = re.sub(r'[{}]'.format(self.symbols), '', self.text)

    def longest_word(self):
        """выводит самое длинное слово, при уcловии что оно одно,
        если несколько то первое, можно вывести список всех."""
        return [word for word in self.only_words.split()
               if len(word) == max(map(lambda x: len(x), self.only_words.split()))][0]

    def often_word(self):
        """выводит самое часто встречающееся слово"""
        return sorted(Counter(self.only_words.lower().split()).items(), key=lambda x: x[1], reverse=True)[0][0]


    def all_palindromes(self):
        """выводит все палиндромы через запятую."""
        return ', '.join(filter(lambda x: x.lower() == x[::-1].lower(), self.only_words.split()))

    def symbols_quantity(self):
        """выводит количество спецсимволов в тексте """
        return len(self.text) - len(self.only_words)
