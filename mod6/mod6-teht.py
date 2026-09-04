# mod 6 t1
import random

maara = int(input("Kuinka monta arpakuutiota heitetään? "))

summa = 0

for i in range(maara):
    silmaluku = random.randint(1, 6)
    summa = summa + silmaluku

print("Silmälukujen summa on:", summa)


# mod 6 t2
numbers = []

while True:
    input_number = input("Anna luku: ")
    if input_number == "":
        #lopeta kysely
        break
    # lisätään syötetty luku listalle
     numbers.append(int(input_number))
numbers.sort(reverse=True)

# quick'n'dirty 
#print(numbers(0:5)) 

# for-lauseella viisi ensimmäistä alkiota
for num in range(5):
    print(numbers[num]) 

# mod 6 t3
luku = int(input("Anna kokonaisluku: "))

alkuluku = True

if luku < 2:
    alkuluku = False
else:
    for i in range(2, luku):
        if luku % i == 0:
            alkuluku = False
            break

if alkuluku:
    print("Luku on alkuluku.")
else:
    print("Luku ei ole alkuluku.")

# mod 6 t4
kaupungit = []

for i in range(5):
    kaupunki = input("Anna kaupungin nimi: ")
    kaupungit.append(kaupunki)

for kaupunki in kaupungit:
    print(kaupunki) 
