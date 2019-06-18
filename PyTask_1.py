import random


class num_random:

    game = 1
    while (game == 1):
        num = random.randint(0, 2)
        attemp = 3

        while(attemp > 0):
            print(f"Количество попыток: {attemp}")

            answer = int(input("Введите число от 0 до 9: "))

            if num == answer:
                print(f"Победа! Ответ {answer} - верный!")
                break
            elif answer > num:
                print("Ответ не верный, искомое число - меньше.")
            else:
                print("Ответ не верный, искомое число - больше.")

            attemp -= 1

        game = input("Игра окончена! Хотите начать заново? (Y/N): ")

        #Y = 1
        #N = 0

        if game == Y:
            print("Начинаем игру заново...")
        else:
            print("До встречи!")
            game = 0
