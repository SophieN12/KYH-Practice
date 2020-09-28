# Uppgift 39:
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > a and c > b:
        return c


def sum_all_list(ls):
    total = 0
    for i in range(0, 5):
        total += ls[i]
    return total


def multiply_all_list(ls):
    product = 1
    for i in range(0, 5):
        product *= ls[i]
    return product


# Uppgift 40:
def reverse(string):
    if len(string) <= 1:
        return string
    return reverse(string[1:]) + string[0]


def caps(string):
    result1 = []
    for c in string:
        if c.isupper():
            result1.append(c)
    result = len(result1)
    return result


def in_range(value):
    result = []
    for i in range(50, 100):
        result.append(i)
        if value in result:
            correct = True
        else:
            correct = False
    return correct

