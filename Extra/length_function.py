def length(txt):
    counter = 0
    for c in txt:
        counter += 1
    return counter


def main():
    my_string = input("Please enter a sentence:")
    length_txt = length(my_string)
    print(length_txt)


if __name__ == "__main__":
    main()
