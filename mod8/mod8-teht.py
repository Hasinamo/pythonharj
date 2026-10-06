# Tehtävä 1
vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")

kuukausi = int(input("Anna kuukauden numero: "))

print(vuodenajat[kuukausi - 1])

# Tehtävä 2
nimet = set()

while True:
    nimi = input("Anna nimi: ")

    if nimi == "":
        break

    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

for nimi in nimet:
    print(nimi)

# Tehtävä 3
lentoasemat = {}

while True:
    toiminto = input("Valitse toiminto (uusi, haku, lopeta): ")

    if toiminto == "uusi":
        icao = input("Anna lentoaseman ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi

    elif toiminto == "haku":
        icao = input("Anna lentoaseman ICAO-koodi: ")

        if icao in lentoasemat:
            print(lentoasemat[icao])
        else:
            print("Lentoasemaa ei löytynyt.")

    elif toiminto == "lopeta":
        break