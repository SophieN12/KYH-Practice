from pathlib import Path
import json

p = Path("phonenumbers.json")
content = p.read_text(encoding="utf8")
people = json.loads(content)


def main():
    while True:
        print(f"Det finns {len(people)} nummer i telefonkatalogen.")

        svar = input("[S]lå upp eller [L]ägg till? ")
        svar = svar[0].upper()
        if svar == 'S':
            vem = input("Vem vill du ringa?")
            if vem not in people:
                print("Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog")
            else:
                number = people[vem]
                print(f"Numret till {vem} är {number}")

        elif svar == 'L':
            namn = input("Ange personens förnamn: ")
            tfn = input("Ange telefonnummer: ")
            people[namn] = tfn
            content = json.dumps(people)
            p.write_text(content, encoding="utf8")

        else:
            print("Förstår inte, avbryter programmet.")
            break


if __name__ == '__main__':
    main()
