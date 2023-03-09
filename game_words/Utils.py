from Basic import BasicWord
import requests
from random import choice as rand


def load_random_word():
    """
    С помощью requests подгружаем наши данные с сайта, отключаем верификацию,
    что бы не сыпало ошибок по поводу SSL сертификации.
    Cохраняем и конвертируем из json формата в переменную words.
    Создаем экземпляр класса BasicWord, с помощью функции random.choice выбираем случайное загаданное слово.
    Возвращаем экземпляр.
    """
    imported_words = requests.get("http://jsonkeeper.com/b/VF4M", verify=False)
    words = imported_words.json()
    word = rand(words)
    random_words = BasicWord(word['word'], word['subwords'])
    return random_words
