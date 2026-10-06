import random
# Mod 5 tehtävä 6 aloitus ja idea
# π≈4n/N, jossa n on ympyrän sisään osuvat pisteet ja N kaikki arvotut pisteet
# Piste on ympyrän sisällä, jos x^2+y^2<1

N = 1000 # kaikkien pisteiden lukumäärä
n = 0 # lasketaan ympyrään osuneiden pisteiden lukumäärä
counter = 0

while counter < N:
    counter += 1
    # arvotaan satunnainen piste välillä -1,-1 ja 1,1
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    print(f"{counter}. arvotun pisteen koordinaatit, x: {x}, y: {y}")
    if x ** 2 + y ** 2 < 1:
        n = n + 1
        print("Piste on ympyrän sisällä.")

print(f"Pisteitä arvottu yhteensä {N}, joista ympyrän sisälle osui {n} kpl.")

#TODO: Laskee pii annetulla kaavalla ja tulosta. Kokeile myös eri N arvoilla.