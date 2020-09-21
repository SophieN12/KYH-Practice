def reg_nummer():
    reg_nr = input("Mata in en reg.nr:")
    print(f"Bokstavsgrupp: {reg_nr[:3]}\nSiffergrupp: {reg_nr[-3:]}")


def main():
    numbers = input("Mata in heltal med komma mellan:").split(",")

    int_list = [int(number)for number in numbers]

    print(f"Första talet: {numbers[0]}\nSista talet: {numbers[-1]}\n"
          f"Summan av talen: {sum(int_list)}")
    numbers.reverse()
    numbers1 = ", ".join(numbers)
    print(f"Talen baklänges: {numbers1}")


if __name__ == "__main__":
    main()
