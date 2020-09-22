string = input("Mata in en textsträng:").lower().replace(" ", "")
length = len(string)
print(length)

if string == string[::-1]:
    print("Textsträngen är en palindrom!")
else:
    print("Textsträngen är ej en palindrom!")
