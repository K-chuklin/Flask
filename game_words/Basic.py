class BasicWord:
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return f'Я основное слово{self.word} и его вариации подслов {self.subwords}'

    def words_counter(self):
        """Возвращает длину списка подслов"""
        return len(self.subwords)

    def word_is_correct(self, word):
        """Проверяет есть ли введенное слово в списке подслов"""
        if word in self.subwords:
            return True
