def reg_nummer():
    reg_nr = input("Mata in en reg.nr:")
    print(f"Bokstavsgrupp: {reg_nr[:3]}\nSiffergrupp: {reg_nr[-3:]}")


def main():
    numbers = input("Mata in heltal med komma mellan:").split(",")

    int_list = [int(number)for number in numbers]

    reversed_numbers = list(reversed(numbers))
    numbers = ", ".join(numbers)
    reversed_numbers = ", ".join(reversed_numbers)

    print(f"Första talet: {numbers[0]}\n"
          f"Sista talet: {numbers[-1]}\n"
          f"Summan av talen: {sum(int_list)}\n"
          f"Talen baklänges: {reversed_numbers}\n"
          f"Udda tal: {numbers[0:100:2]}\n"
          f"Jämna tal: {numbers[1:100:2]}")


if __name__ == "__main__":
    main()
