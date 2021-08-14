from random import *

word_list = ["человек", "слово", "лицо", "дверь", "земля", "работа", "ребенок", "история",
             "женщина", "развитие", "власть", "правительство", "начальник", "спектакль",
             "автомобиль", "экономика", "литература", "граница", "магазин", "председатель",
             "сотрудник", "республика", "личность"]

def get_word(words):
    return choice(words).upper()

def display_hangman(tries):
    stages = [# финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Давайте играть в угадайку слов!\n")
    while not guessed and tries > 0:
        print(display_hangman(tries))
        print(f"Количество попыток: {tries}")
        print(f"Ошибки: {guessed_letters}")
        print(f"Слово: {word_completion}")
        if "_" not in word_completion:
            print("Поздравляем, вы угадали слово! Вы победили!")
            guessed = True 
            break 
        user_answ = input("Введите букву или слово: \n").upper()
        while not user_answ.isalpha():
            user_answ = input("Вы ввели недопустимый символ, введите букву!: ").upper()
        if len(user_answ) > 1:
            if user_answ not in guessed_words:
                if user_answ == word:
                    print("Поздравляем, вы угадали слово! Вы победили!")
                    word_completion = user_answ
                else:
                    print("Это не правильное слово, -1 попытка")
                    guessed_words.append(user_answ)    
                    tries -= 1
            else:
                print("Вы уже называли данное слово")
                continue
        else:
            if user_answ not in guessed_letters:
                if user_answ in word:
                    for i in range(len(word)):
                        if user_answ == word[i]:
                            word_completion = word_completion[:i] + user_answ + word_completion[i+1:]            
                else:
                    print("Это не правильная буква, -1 попытка")
                    guessed_letters.append(user_answ)
                    tries -= 1
            else:
                print("Вы уже называли данную букву")
                continue
    if guessed == False:
        print(f"\nВы проиграли! Загаданное слово: {word}")
        print(display_hangman(tries))
        

again = "1"
while again == "1":
    play(get_word(word_list))
    again = input("Сыграем ещё раз? \n 1.Да 2.Нет\n")