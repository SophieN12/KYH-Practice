def ask_user(user):
    (name, age) = user
    print(f"Namn: {name}")
    print(f"Ålder: {age}")


def change_place(t):
    (a, b) = t
    (a, b) = (b, a)
    t = (a, b)
    return t


def convert(ls):
    return tuple(ls)


