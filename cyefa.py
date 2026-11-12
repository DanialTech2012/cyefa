import re
import random
import time

email_pattern = r"([\w.+-]+)@([\w-]+\.[a-zA-Z]{2,})"
password_pattern = r"(?=.*[A-Za-z])(?=.*\d).{8,}"

while True:
    email = input("Enter your email: ")
    match = re.fullmatch(email_pattern, email)

    if match:
        print(f"Email корректный")
        print(f"Имя пользователя: {match.group(1)}")
        print(f"Домен: {match.group(2)}")
        break
    else:
        print("Неправильный формат email, попробуйте снова\n")

while True:
    password = input("Enter your password: ")
    match = re.fullmatch(password_pattern, password)

    if match:
        print("Пароль подходит")
        break
    else:
        print("Пароль должен содержать минимум 8 символов, хотя бы одну букву и одну цифру\n")

print("\nРегистрация завершена!")
print(f"Email: {email}")
print("Password: " + "*" * len(password))

questions = {
    "В каком году началась вторая мировая война?": "1945",
    "Сколько океанов на планете?": "5",
    "Сколько планет в солнечной системе?": "8",
    "Самая длинная река в мире?": "Амазонка",
    "2 + 2 =": "4",
}

score = 0


def add_question():
    q = input("\nДобавьте свой вопрос: ")
    a = input("Добавьте к нему ответ: ")
    questions[q] = a
    print(f"Успешно добавлен вопрос!")


TIME_LIMIT = 60


def run_quiz():
    score = 0
    items = list(questions.items())
    random.shuffle(items)

    for question, answer in items:
        print(f"\n{question}")
        start_time = time.time()
        user_answer = input(f"Ваш ответ (у вас {TIME_LIMIT} сек): ")
        elapsed = time.time() - start_time

        if elapsed >= TIME_LIMIT:
            print(f"Время вышло! Правильный ответ: {answer}")
            continue

        if user_answer.strip().lower() == answer.strip().lower():
            print("Правильно!")
            score += 1
        else:
            print(f"Неверно. Правильный ответ: {answer}")

    print(f"\nИтог: {score} из {len(items)} правильных ответов")


def show_question():
    print(f"\n=== Вопросы и ответы ===")
    if not questions:
        print('Список вопросов пуст.')
        return
    for i, j in questions.items():
        print(f"{i}  ===  {j}")


def play_quiz():
    global score
    if not questions:
        print('\nВопросов больше нет!')

    question = random.choice(list(questions.keys()))
    answer = questions[question]

    print(f"\nМой вопрос к тебе: {question}")
    player_answer = input("Answer: ")
    if player_answer == answer:
        score += 1
        del questions[question]
        print("+1 score")
    else:
        print("Неправильно попробуй еще раз!")


while True:
    print('\n' + '=' * 60)
    print('Главное меню')
    print('=' * 60)
    print('1. Посмотреть все вопросы')
    print('2. Добавить свой вопрос')
    print('3. Сыграть в викторину (случайный вопрос)')
    print('4. Посмотреть мой счёт')
    print('5. Запустить викторину 60 сек')
    print('6. Выйти')

    choice = input('Выберите действие (1-6): ')

    if choice == '1':
        show_question()
    elif choice == '2':
        add_question()
    elif choice == '3':
        play_quiz()
    elif choice == '4':
        print(f'\nВаш текущий счёт: {score}')
    elif choice == '5':
        run_quiz()
    elif choice == '6':
        print('\nСпасибо за игру! До свидания!')
    else:
        print('\nНеверный ввод, введите число от 1 до 6.')