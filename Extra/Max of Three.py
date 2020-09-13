def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


def main():
    A = int(input("Please input a number:"))
    B = int(input("Please insert a second number:"))
    C = int(input("Please insert a third number:"))
    biggest = max_of_three(A, B, C)
    print(f"{biggest} is the bigger number of the two inserted number!")


if __name__ == "__main__":
    main()

