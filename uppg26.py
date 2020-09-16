import requests


def main():
    movie = input("What movie do you wanna see?:")
    args = {"t": movie, "apikey": "9f6d550c"}
    r = requests.get("http://www.omdbapi.com/", params=args)
    data = r.json()

    print("*** Resultat från OMDB! ***")
    print(F"Titel: {data['Title']} regisserades av {data['Director']}")
    print(F"Skådisar: {data['Actors']}")
    print(F"IMDB Betyg: {data['imdbRating']}")
    print(F"Awards: {data['Awards']}")
    print(F"Längd: {data['Runtime']}")


main()





































