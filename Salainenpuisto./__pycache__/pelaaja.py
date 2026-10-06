class Pelaaja:
    """Pelaaja-olio sisältää pelaajan omat tiedot."""

    def __init__(self, nimi, ika, sijainti):
        self.nimi = nimi
        self.ika = ika
        self.sijainti = sijainti
        self.inventaario = []
        self.pisteet = 100

    def liiku(self, uusi_paikka):
        """Siirtää pelaajan uuteen paikkaan."""
        self.sijainti = uusi_paikka

        print()
        print("Siirryit paikkaan:", uusi_paikka.nimi)

        if uusi_paikka.esine is not None:
            print("Tässä paikassa näkyy esine:",
                  uusi_paikka.esine.nimi)

    def keraa_esine(self):
        """Kerää nykyisessä paikassa olevan esineen."""

        if self.sijainti.esine is None:
            print("Tässä paikassa ei ole esinettä.")
            return False

        esine = self.sijainti.esine

        self.inventaario.append(esine)
        self.sijainti.esine = None
        self.pisteet += 10

        print("Keräsit esineen:", esine.nimi)
        print("Sait 10 pistettä.")

        return True

    def nayta_inventaario(self):
        """Näyttää pelaajan inventaarion."""

        print()
        print("=== INVENTAARIO ===")

        if len(self.inventaario) == 0:
            print("Inventaario on tyhjä.")

        else:
            for esine in self.inventaario:
                print("-", esine.nimi)

        print("Pisteet:", self.pisteet)

    def onko_esine(self, nimi):
        """Tarkistaa, onko pelaajalla tietty esine."""

        for esine in self.inventaario:

            if esine.nimi == nimi:
                return True

        return False