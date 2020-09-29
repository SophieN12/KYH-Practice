# Uppgift 44

def ask_user(user):
    (name, age) = user
    print(f"Namn: {name}")
    print(f"Ålder: {age}")


ask_user(user=("Sophie", 20))


def change_place(t):
    (a, b) = t
    (a, b) = (b, a)
    t = (a, b)
    return t


t = (16,23)
print(change_place(t))


def convert(ls):
    return tuple(ls)


ls = ["Sophie", "Kevin", "Nancy"]
print(type(convert(ls)))
print(convert(ls))
