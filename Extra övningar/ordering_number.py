def main():
    X = 25
    Y = 245
    Z = 36

    if X < Y and X < Z:
        x = X
        if Y < Z:
            y = Y
            z = Z
        else:
            y = Z
            z = Y

    if Y < X and Y < Z:
        x = Y
        if X < Z:
            y = X
            z = Z
        else:
            y = Y
            z = X

    print(x, y, z)


if __name__ == "__main__":
    main()
