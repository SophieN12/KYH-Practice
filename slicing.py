def reg_nummer():
    reg_nr = input("Mata in en reg.nr:")
    print(f"Bokstavsgrupp: {reg_nr[:3]}\nSiffergrupp: {reg_nr[-3:]}")


def main():
    numbers = input("Mata in heltal med komma imellan:").split(",")
    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])
    print(f"Första talet: {numbers[0]}\nSista talet: {numbers[-1]}\n"
          f"Summan av talen: {sum(numbers)}")
    numbers.reverse()
    print(f"Talen baklänges:{numbers}")
    #print(*numbers, sep=', ')


if __name__ == "__main__":
    main()
