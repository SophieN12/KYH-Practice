def is_it_too_long(name):
    return len(name) > max_length


def main():
    # students = ["anna", "beatrice", "cecilia", "doris", "esmeralda", "frida", "gunilla"]
    students = input("Mata in en lista av studentens namn med komma tecken och ingen mellanrum:").split(",")

    for name in students:
        if is_it_too_long(name):
            name = name.strip(" ")
            print(f"{name.capitalize()} är för långt!")


if __name__ == '__main__':
    try:
        max_length = int(input("Hur många bokstäver är för långt?:"))
    except ValueError:
        print("Obs, något blev fel, det blir satt till 5")
        max_length = 5
main()
