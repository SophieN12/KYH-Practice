def upper(text):
    # string = input("Please enter a string:")

    vowels = "aouyie"
    string = ""
    for c in text:
        if c in vowels:
            string += c.upper()
        else:
            string += c
    return string


def main():
    print(upper("Hello, whats your name?"))


if __name__ == "__main__":
    main()
