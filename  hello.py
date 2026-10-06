print('moikka')
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

#uusi_kayttaja = input('Anna nimesi: ')
#print("Hauska tavata, " + uusi_kayttaja + "!")























































'''

print (tuloste)

# Laskumme

# luetaan käyttäjältä kaksi lukua (str) jotka täytyy muistaa muuntaa
# liukuluvuksi eli Float ja sijoitetaan muuttujiin

a =  float(input(('Anna ensimmäinen luku:\n')
b = float (input(('Anna toinen luku:\n') )

yhteenlasku = a + b 
vähennyslasku = a - b 
kertolasku = a * b 
potenssiinkorotus = a ** b # esim 2^3
jakolasku = a / b 
kokonaisosa = a // b 
jakojaannos = a % b 

print (f'Yhteenlasku: {yhteenlasku}') 
print (f'Vähennyslasku: {vähennyslasku}' ) 
print (f'Kertolasku: {kertolasku}') 
print (f'potenssinkorotus: {potenssinkorotus}') 
print (f'jakolasku: {jakolasku}') 
print (f' Kokonaisosa: {kokonaisosa}') 
print (f' Jakojäännös: {jakojaannos}') 