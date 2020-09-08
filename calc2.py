import random


def game(how_many, max_value):
    correct_answers = 0

    for i in range(int(how_many)):
        a = random.randint(1, max_value)
        b = random.randint(1, max_value)

        while True:
            answer = input(f"{a}+{b}:")
            try:
                number = int(answer)
                break
            except ValueError:
                print("Testa igen!")

        if number == a + b:
            print("Rätt!")
            correct_answers += 1
        else:
            print(f"Fel... Det blir {a + b}")
            print("---")
    print(f"Du fick {correct_answers} av {how_many} rätt.")


if __name__ == '__main__':
    while True:
        how_many = (input("Hur många frågor?:"))
        try:
            how_many = int(how_many)
            break
        except ValueError:
            print("Inte ett heltal, försök igen!")
    while True:
        max_value = (input("Högsta siffra?:"))
        try:
            max_value = int(max_value)
            break
        except ValueError:
            print("Inte ett heltal, försök igen!")
    game(how_many, max_value)
