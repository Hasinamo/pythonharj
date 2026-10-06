# tehtävä 1, 2 ja 3

class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def siirry_kerrokseen(self, kohde):
        if kohde < self.alin or kohde > self.ylin:
            print("Kerrosta ei ole hissin alueella.")
            return

        while self.kerros < kohde:
            self.kerros_ylös()

        while self.kerros > kohde:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.kerros < self.ylin:
            self.kerros += 1
            print("Hissi on nyt kerroksessa", self.kerros)

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
            print("Hissi on nyt kerroksessa", self.kerros)


class Talo:
    def __init__(self, alin, ylin, hissien_maara):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []

        for i in range(hissien_maara):
            hissi = Hissi(alin, ylin)
            self.hissit.append(hissi)

    def aja_hissia(self, hissin_numero, kohdekerros):
        if hissin_numero < 1 or hissin_numero > len(self.hissit):
            print("Hissin numeroa ei ole olemassa.")
            return

        hissi = self.hissit[hissin_numero - 1]
        hissi.siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        print("PALOHÄLYTYS!")
        print("Kaikki hissit palaavat pohjakerrokseen.")

        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin)


# Pääohjelma

# Tehtävä 1: Hissin testaaminen
print("TEHTÄVÄ 1")
h = Hissi(1, 10)

h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)


# Tehtävä 2: Talon ja hissien testaaminen
print("\nTEHTÄVÄ 2")

talo = Talo(1, 10, 3)

talo.aja_hissia(1, 5)
talo.aja_hissia(2, 8)
talo.aja_hissia(3, 4)


# Tehtävä 3: Palohälytys
print("\nTEHTÄVÄ 3")

talo.palohalytys()