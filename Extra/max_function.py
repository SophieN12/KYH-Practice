def max(a, b):
    if a > b:
        return a
    else:
        return b


def main():
    A = int(input("Please input a number:"))
    B = int(input("Please insert a second number:"))
    biggest = max(A, B)
    print(f"{biggest} is the bigger number of the two inserted number!")


if __name__ == "__main__":
    main()


