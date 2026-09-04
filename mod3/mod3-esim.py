import math

# Tuntiesimerkit 19.8.2026

'''
teksti = "Tämä on laskukone, anna kaksi lukua."

luku = input("Anna 1. luku: ")
luku2 = input("Anna 2. luku: ")

luku = float(luku) # esim. "10.5" -> 10.5
luku2 = float(luku2)

summa = luku + luku2
#print("summa", summa)

#print("Lukujen", luku, luku2, "summa on", summa)

# sama liitosoperaattorilla (+)
summa = str(summa) 
#print("summa:   " + summa)

print("Lukujen " + str(luku) + " ja " + str(luku2) + " summa on " + summa + ".")
print('Terve', summa, luku)


ikä = 22
uusi_kayttaja = input('Anna nimesi: ')
print("Hauska tavata, " + uusi_kayttaja + "!")

# Tulosteen muotoilu fstringillä (kannattaa)
###############

# nyt ei tarvitse tehdä tyyppimuunnoksia
print('Hauska tavata {uusi_kayttaja}!!!!!') #puuttuu f, ei toimi
print(f'Hauska tavata {uusi_kayttaja} ja ikäni on {ikä}!!!!!')
'''
# muuttujan tyypit
##############

pisteet = 200
pisteet = 400 # muuttujan tietoja ylikirjoitetaan
print(pisteet)

merkkijono = 'Ulla'
# merkkijono = '9' # on yhä merkkijono vaikka sisältää numeron
# merkkijono = '' # tyhjä merkkijono
pisteet = 0

print(f'Merkkijono: {merkkijono:<20s} sijoitetaan tähän väliin')

kokonaisluku = -9
kokonaisluku_pitkä = 12_456_123_180
liukuluku = 4.973
kompleksiluku = -4 + 2j
totuusarvo = False

print(kompleksiluku)
print(kompleksiluku.real)
print(kompleksiluku.imag)

# printataa muuttujan tyyppi
print(f'Muuttujan tyyppi voidaan tutkia {type(kompleksiluku)}')

print(f'{"Vakio":6s}| {"Arvo":6s}')
print('-------------')
print(f'{"Pii":6s}: {math.pi:<6.2f}')

# Laskutoimitukset
##################

tuloste = '''
    yhteenlasku (+), vähennyslasku (-)
    kertolasku (*), jakolasku (/)
    jakojäännösoperaatio (%)
    pelkän kokonaisosan palauttava jakolasku (//) 
    potenssiinkorotus (**)
'''

print(tuloste)

# Laskukone

# luetaan käyttäjältä kaksi lukua (str) jotka täytyy muistaa muuntaa
# liukuluvuksi eli Float ja sijoitetaan muuttujiin

a = float(input('Anna ensimmäinen luku:\n'))
b = float(input('Anna toinen luku:\n'))

yhteenlasku = a + b
vahennyslasku = a - b
kertolasku = a * b
potenssiinkorotus = a ** b # esim 2^3
jakolasku = a / b
kokonaisosa = a // b
jakojaannos = a % b

print(f'Yhteenlasku: {yhteenlasku}')
print(f'Vähennyslasku: {vahennyslasku}')
print(f'Kertolasku: {kertolasku}')
print(f'Potenssinkorotus: {potenssiinkorotus}')
print(f'Jakolasku: {jakolasku}')
print(f'Kokonaisosa: {kokonaisosa}')
print(f'Jakojäännös: {jakojaannos}') 