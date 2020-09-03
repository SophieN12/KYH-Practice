def main():
    notes ={"1": "George Washinton",
           "2": "Thomas Jefferson",
           "5": "Abraham Lincoln",
           "10": "Alexander Hamilton",
           "20": "Andrew Jackson",
           "50": "Ulysses S. Grant",
           "100": "Benjamin Franklin"
    }
    value = (input("Type in the value of an US dollar bill:"))

    if value not in notes:
        print("Sorry, the entered amount does not correspond with the value of an US dollar bill")
    else:
        print("The person on that bill is:", notes[value])


if __name__ == "__main__":
    main()
