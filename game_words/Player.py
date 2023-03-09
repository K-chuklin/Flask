class Player:
    def __init__(self, name, word):
        self.name = name
        self.word = word
        self.used_words = []

    def __repr__(self):
        return f'Я игрок {self.name} и я ввожу слова {self.word}, которые сохраняются в {self.used_words}'

    def used_words_counter(self):
        """Возвращает длину списка использованных слов"""
        return len(self.used_words)

    def add_word_to_used_words(self, word):
        """Добавляет введенное слово к списку использованных слов"""
        return self.used_words.append(word)

    def word_already_used(self, word):
        """Проверяет есть ли слово в списке использованных слов"""
        if word in self.used_words:
            return True



