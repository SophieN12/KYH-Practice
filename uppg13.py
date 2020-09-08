import random


def main():
    kate1 = ("svensken", "norsken")
    kate2 = ("spanish flu", "vattenkoppor")
    kate3 = ("Sophie", "Alexander")
    kate4 = ("pressekreterare", "chef")

    kate1 = random.choice(kate1)
    kate2 = random.choice(kate2)
    kate3 = random.choice(kate3)
    kate4 = random.choice(kate4)

    text = str(
        f"En app som kan laddas ned till mobiltelefonen ska varna {kate1} som kommit nära någon som smittats med {kate2}. – Jag tycker att ni i Sverige borde överväga att göra något liknande, säger {kate3}, {kate4} för Finska institutet för hälsa och välfärd, THL.")

    print(text)


if __name__ == "__main__":
    main()
