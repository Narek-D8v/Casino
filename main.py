from random import randint
import webbrowser

money = 5000

def start():
    print("\n" * 100)
    print("Добро пожаловать в Казино!\n")
    a = int(input("Что вас интересует?\n 1 - баланс\n 2 - начать игру\n 3 - правила\n Ответ: "))
    if a == 1:
        balance()
    elif a == 2:
        bet()
    elif a == 3:
        rules()
    else:
        print("Неверный ввод. Возврат в меню.")
        start()

def balance():
    global money
    print("\n" * 100)
    b = int(input(f"Ваш баланс: {money}$\n 1 - назад\n 2 - пожертвовать 100$ детям\n Ответ: "))
    if b == 1:
        start()
    elif b == 2:
        if money >= 100:
            webbrowser.open("https://www.youtube.com/watch?v=rp1EcmUHv7Q")
            money -= 100
            print("Спасибо за добрый поступок!\n")
            start()
        else:
            print("Недостаточно средств.")
            start()
    else:
        print("Неверный ввод.")
        start()

def bet():
    global money
    print("\n" * 100)
    stake = int(input("Ставка (минимум 100$): \n"))
    if stake >= 100 and money >= stake:
        money -= stake
        game(stake)
    else:
        print("Ставка слишком мала или недостаточно средств.")
        bet()

def game(stake):
    secret = randint(0, 100)
    guess = int(input("Угадай число от 0 до 100: "))
    distance = abs(secret - guess)
    
    # Множитель в зависимости от расстояния
    if distance == 0:
        multiplier = 3.0
    elif distance <= 2:
        multiplier = 2.0
    elif distance <= 4:
        multiplier = 1.8
    elif distance <= 6:
        multiplier = 1.6
    elif distance <= 8:
        multiplier = 1.4
    elif distance <= 10:
        multiplier = 1.2
    else:
        multiplier = 0.0

    winnings = stake * multiplier
    print(f"Загаданное число: {secret}")
    print(f"Ваше число: {guess}")
    print(f"Расстояние: {distance}")
    if multiplier > 0:
        print(f"Выигрыш: {winnings}$ (множитель {multiplier}x)")
        global money
        money += winnings
    else:
        print("Вы промахнулись. Ставка сгорела.")

    again = int(input("Сыграть ещё? (1 - да / 2 - нет): "))
    if again == 1:
        bet()
    else:
        start()

def rules():
    print("\n" * 100)
    print("Правила игры:\nУгадай число от 0 до 100.")
    print("Чем ближе к загаданному, тем выше множитель выигрыша.")
    print("Точное попадание даёт 3x от ставки!")
    input("Нажмите Enter для возврата...\n")
    start()

start()
