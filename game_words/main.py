if __name__ == '__main__':
    from Utils import load_random_word
    from Player import Player

    question = load_random_word()  # Создаем экземпляр класса
    print('Введите ваше имя: ')  # Просим пользователя проинициализировать себя
    user = Player(input(), None)  # Создаем экземпляр класс
    all_subwords = question.words_counter()  # Создаем счетчик, который подсчитает все под-слова
    user.used_words = []  # Создаем список, в который будем заносить все введенные пользователем слова
    zero = 0  # Создаем переменную к которой будем итерироваться

    print(f'Привет {user.name.title()}!')
    print(f'Составьте {question.words_counter()} слов из слова {question.word.upper()}')
    print('Слова должны быть не короче 3 букв')
    print('Что бы закончить игру угадайте слова или напишите "стоп"')
    print('Поехали ваше первое слово?')
    # print(question.subwords)  # Cтрока, позволяющая проверить какие под-слова были загаданы

    while question.words_counter() > zero:
        """"
        Запускаем цикл в котором, если пользователь угадывает слово, 
        оно удаляется из списка под-слов и мы приближаемся к переменной zero, 
        так мы итерируемся по циклу
        """

        user.word = input().lower()  # Просим пользователя ввести слово

        if user.word_already_used(user.word):
            print('Уже использовано')

        elif len(user.word) <= 2:
            print("слишком короткое слово")
            continue

        elif user.word == 'стоп':
            print(f'Игра завершена, вы угадали {all_subwords - question.words_counter()} слов!')
            break

        elif question.word_is_correct(user.word):
            question.subwords.remove(user.word)
            user.add_word_to_used_words(user.word)
            print('Верно')

        elif not question.word_is_correct(user.word):
            user.used_words.append(user.word)
            print('Неверно')

    print(f'Игра завершена, вы угадали {all_subwords - question.words_counter()} слов!')

