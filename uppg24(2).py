import requests

r = requests.get("https://proagile.se/api/publicEvents")
course_list = r.json()


def main(startdate, enddate):
    for course in course_list:
        coursedate = course["startDate"]
        if startdate <= coursedate <= enddate:
            print()
            kursnamn = "Kursnamn:"
            startdatum = "Startdatum:"
            slutdatum = "Slutdatum:"
            print(f"{kursnamn:>12}, {course['name']}")
            print(f"{startdatum:>12}, {coursedate}")
            print(f"{slutdatum:>12}, {course['endDate']}")


if __name__ == "__main__":
    year = input("Year:")
    month = input("Month:")
    start = f"{year}-{month}-01"
    end = f"{year}-{month}-31"
    print(start, end)
    main(startdate=start, enddate=end)



