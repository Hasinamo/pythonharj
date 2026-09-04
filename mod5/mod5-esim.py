import random

suorita = True

while suorita:
    print('Tämä printtaantuu vain kerran')
    suorita = False

print('Suoritus loppui')

# while == toista niin kauan kun ehto on tosi

luku = 1                # 1. alkuarvo / kierrosmuuttuja

while luku <= 5:        # 2. ehto
    print(luku)
    # luku = luku + 1     # 3. muuttujan arvon muuttaminen
    luku += 1

print('Jatketaan ohjelmaa')

# 1. Muuta ohjelmaa niin että tulostetaan luvut 10-1
# 2. Muuta ohjelmaa niin että luku 10 kysytään käyttäjältä
###########################

luku = int(input('Anna luku josta laskemma alaspäin: '))          

while luku >= 1:       
    print(luku) 
    luku -= 1



# käyttäjä lopettaa toiston
############

salasana = input('Anna salainen salasana jotta pääset sisään (python): ').strip()

# !=	eri suuri kuin
while salasana != 'python':
    print('Väärä salasana')
    salasana = input('Anna salasana uudestaan: ')

print('Tervetuloa sisään, koodi oli oikein')


# while / else rakenne
# suoritua siirtyy else-haaraan kun toistoehto on epätosi
# sitä ei suoriteta jos poistutaan break-lauseella
# else rakenne on harvemmin käytetty

komento = input('Anna komento (lopeta, APUA): ').strip().lower()
# apua APUA

while komento != 'lopeta':
    if komento == 'apua':
        break
    print('Annoit komennon: ', komento)
    komento = input('Anna uusi komento: ')
else:
    print('Annoit käskyn lopeta, joten näin tehdään!!!')


print('Ohjelma jatkuu')


noppa1 = noppa2 = heitot = 0

# 2 ja 6
# or (jompikumpi eli toteutuu)
# TRUE FALSE 

# 2 ja 6
# and (pitäis olla molemmat eli ei toteudu ja silmukka loppuu)
# TRUE FALSE 


while (noppa1 != 6 or noppa2 != 6):

    noppa1 = random.randint(1,6)
    noppa2 = random.randint(1,6)
    print(noppa1, noppa2)
    heitot = heitot + 1

print(f"Tarvittiin {heitot:d} heittoa.")

# sama nopanheitto uudestaan, nyt sisäkäisellä toistorakenteella

eka = 1
while eka <= 5:
    toka = 1
    while toka <= 5:
        print(f"{eka} kertaa {toka} on {eka*toka:d}")
        toka = toka + 1
    eka = eka + 1


pelikerta = 0
heitot = 0
while pelikerta < 1000:

    noppa1 = noppa2 = 0
    while (noppa1 != 6 or noppa2 != 6):
        noppa1 = random.randint(1,6)
        noppa2 = random.randint(1,6)
        # print(noppa1, noppa2)
        heitot = heitot + 1
    pelikerta += 1

print('Pelikertoja meillä oli:', pelikerta)
print(f"Tarvittiin {heitot:d} heittoa.")
print(f'Jokaisella kierroksella oli keskimäärin {heitot/pelikerta} heittoa')

# tehtävä 1
############

luku = 1
while luku <= 1000:
    # onko luku kolmella jaollinen, jos on niin printta
    if luku % 3 == 0:
        print(luku)
    luku += 1


# tehtävä 4 modattuna
## TODO: tee tehtävän loppuun

oikea_numero = 7
arvaus = int(input('Arvaa numero 1 ja 10 välillä: '))

while arvaus != oikea_numero:
    print('Väärin')
    arvaus = int(input('Arvaa uudestaan: '))

print(f'Yes, sait kaiken oikein!!! Numero tosiaan oli {oikea_numero} ')

# usein while rakennetta käytetään ja varsinkin teidän projekteissa!!
# ns. pääsilmukka ELI main loop

peli_käynnissä = True
# main loop
print('Tervetuloa peliini!!!!!')

while peli_käynnissä:
    print('Anna ohjeita pelaajalle, tee jotain')
    # kun peli on pelattu
    peli_käynnissä = False

print('Game over')


        