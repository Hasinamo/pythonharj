import random


# Tehtävä 1
def heita_noppaa():
    return random.randint(1, 6)


while True:
    silmaluku = heita_noppaa()
    print(silmaluku)
    if silmaluku == 6:
        break


# Tehtävä 2
def heita_noppaa2(tahkot):
    return random.randint(1, tahkot)


maksimi = int(input("Anna nopan maksimisilmäluku: "))

while True:
    silmaluku = heita_noppaa2(maksimi)
    print(silmaluku)
    if silmaluku == maksimi:
        break


# Tehtävä 3
def gallonat_litroiksi(gallona):
    return gallona * 3.785


while True:
    gallona = float(input("Anna gallonamäärä: "))
    if gallona < 0:
        break
    litrat = gallonat_litroiksi(gallona)
    print(f"{litrat:.3f} litraa")