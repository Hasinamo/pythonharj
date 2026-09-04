# Tuntiesimerkkejä moduulin 4

import random

# boolean
onko_totta = False
if onko_totta:
    print("Onhan se totta!")


## kolikonheittosimulaattori
random_number = random.randint(0, 1)
print(random_number)

# if lauseen _ehto_ muodostuu AINA True tai False arvoksi
# jos ehto on tosi suoritetaan if-koodilohko, muuten else-lohko
if random_number == 0:
    result = "kruuna"
    print("kruuna tuli")
else:
    result = "klaava"

print(f"Heitit kolikkoa ja sait {result}n.")


## kolikonheittosimulaattori 2.0
# kolikko pystyyn tod.näk. oikeasti jotain 1/6000 luokkaa?
random_number = random.random()
print(random_number) # liukulukuarvo väliltä 0-1

# kolikko jää pystyyn todennäköisyys 1/100
if random_number < 0.01:
    print("Kolikko jäi pystyyn")
elif random_number < 0.505:
    print("Kruuna tuli.")
else:
    print("Klaava tuli")

## erilaisia ehtoja

arvo = 150
print(90 < arvo < 110 )
print(100 != 101)

# kalvoesimerkki

ikä = int(input("Anna ikä: "))
if 15 <= ikä < 18:
    paino = float(input("Anna paino (kg): "))

if ikä >= 18 or (ikä >= 15 and paino >= 55):
    print("Lääkkeen käyttö on sallittua.")


# esimerkki ehdoista (jälkimmäinen if-lause) ikäarvolla 18
#print(True or (True and False))

print(not True) 