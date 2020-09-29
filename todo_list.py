import pathlib

p = pathlib.Path("todo1")
list = p.read_text().splitlines()


def add():
    add = input("Add task:")
    list.append(add)
    p.write_text("\n".join(list))


def delete():
    remo = input("Delete task:")
    list.remove(remo)
    p.write_text("\n".join(list))


def choice():
    choose = input("\n1:Show list\n2:Add task\n3:Delete task\n4:Quit\n>>>")
    if choice == "1":
        print(list)
    elif choose == "2":
        add()
    elif choose == "3":
        delete()


choice()

