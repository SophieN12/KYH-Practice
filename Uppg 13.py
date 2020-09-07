import random

text = str("En app som kan laddas ned till mobiltelefonen ska varna finländare som kommit nära någon som smittats med "
           "coronaviruset. – Jag tycker att ni i Sverige borde överväga att göra något liknande, "
           "säger MarkkuTervahauta, generaldirektör för Finska institutet för hälsa och välfärd, THL.").split(" ")

kate1 = ("svensken", "norsken")
kate2 = ("spanish flu", "vattenkoppor")
kate3 = ("Sophie", "Alexander")
kate4 = ("pressekreterare", "chef")

a = random.randint(0, len(kate1)-1)
text[10] = kate1[a]

b = random.randint(0, len(kate2)-1)
text[18] = kate2[b]

c = random.randint(0, len(kate3)-1)
text[33] = kate3[c]

d = random.randint(0, len(kate4)-1)
text[34] = kate4[d]


print(text)