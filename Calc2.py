import random


def game():
    correct_answers = 0
    how_many = input("Hur många frågeställningar vill du svara på?:")
    max_value = input("Högsta siffra?:")
    max_value = int(max_value)

    for i in range(int(how_many)):
        a = random.randint(1,max_value)
        b = random.randint(1,max_value)
        answer = input(f"{a}+{b}")
        number = int(answer)

        if number == a + b:
            print("Rätt!")
            correct_answers += 1
        else:
            print(f"Fel... Det blir {a + b}")
            print("---")
    print(f"Du fick {correct_answers} av {how_many} rätt.")


if __name__ == '__main__':
    game()
