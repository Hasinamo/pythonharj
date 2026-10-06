class Elain:

    # staattinen eli luokkamuuttuja, jonka arvo on yhteinen kaikille olioille
    elainten_lkm = 0

    def __init__(self, nimi, paino, synt_aika):
@@ -16,7 +17,12 @@ def liiku(self):
    def kaikki_tiedot(self):
        print(f"Nimi: {self.nimi}, paino: {self.paino/1000} kg, syntymäaika: {self.synt_aika}")

# Jotkut eläinlajit voivat olla myös Petoja
class Peto:
    def __init__(self, on_metsastaja):
        self.on_metsastaja = on_metsastaja

# Tässä esimerkissä ilves ei olekaan peto
class Ilves(Elain):
    def kilju(self):
        print(f"Ilves nimeltä {self.nimi} kiljuu!")
@@ -26,12 +32,18 @@ def kaikki_tiedot(self):
        super().kaikki_tiedot()


class Karhu(Elain):
    def __init__(self, nimi, paino, synt_aika, on_horroksessa):
# Karhu perii kaksi luokkaa (moniperintä)
class Karhu(Elain, Peto):
    def __init__(self, nimi, paino, synt_aika, on_horroksessa, on_metsastaja):
        self.on_horroksessa = on_horroksessa
        # koska konstruktori "ylikirjoitetaan", tarvitsee yliluokan konstruktoria kutsua
        # erikseen, jos sitä halutaan hyödyntää
        super().__init__(nimi, paino, synt_aika)
        super().__init__(nimi, paino, synt_aika) # super() viittaa vain ensin perittävään luokkaan
        # voidaan käyttää myös suoraan yliluokan nimeä:
        ##Elain.__init__(self, nimi, paino, synt_aika)
        # muiden perittävien luokkien konstruktoreihin viitataan aina luokan nimellä
        # Huom: vaatii myös "self"-parametrin:
        Peto.__init__(self, on_metsastaja)

    def karju(self):
         print(f"Karhu nimeltä {self.nimi} karjuu!")
@@ -40,25 +52,44 @@ def liiku(self):
        print(f"Karhu {self.nimi} möyrii eteenpäin.")

    def kaikki_tiedot(self):
        print(f"\nKarhu, on talviunilla: {self.on_horroksessa}")
        print(f"\nKarhu on metsästäjä: {self.on_metsastaja}, joka on nyt talviunilla: {self.on_horroksessa}")
        super().kaikki_tiedot()

# Elaintarha eläimiä varten (assosiaatioesimerkki)
class Elaintarha:
    def __init__(self, nimi="nimetön"):
        self.nimi = nimi
        self.elaimet = []

    def lisaa_elain(self, elain):
        self.elaimet.append(elain)

    def listaa_kaikki(self):
        print(f"\nEläintarhan {self.nimi} kaikki eläimet ({len(self.elaimet)} kpl) ")
        print("=======================================")
        for elain in self.elaimet:
            elain.kaikki_tiedot()
            print("---")


uusi_elain = Elain("Joku elukka", 1500, 20250921)
#uusi_elain.liiku()

ilves1 = Ilves("Ilveskissa", 6500, 20230621)
#ilves1.liiku()
#ilves1.kilju()

karhu1 = Karhu("Nalle", 155000, 20200814, False)
karhu1 = Karhu("Nalle", 155000, 20200814, False, True)
#karhu1.karju()
#karhu1.liiku()
#print(karhu1.on_horroksessa)

kaikki_elaimet = [uusi_elain, ilves1, karhu1]
kaikki_elaimet.append(Karhu("Isonalle", 205000, 20210411, True))
tarha = Elaintarha("Korkeasaari")
tarha.lisaa_elain(ilves1)
tarha.lisaa_elain(karhu1)
tarha.lisaa_elain(Karhu("Isonalle", 205000, 20210411, True, True))

for elain in kaikki_elaimet:
    elain.kaikki_tiedot()
tarha.listaa_kaikki()

# Staattisen muuttujaan viitataan luokan nimen kautta
print(f"Eläimiä luotu yhteensä: {Elain.elainten_lkm}")