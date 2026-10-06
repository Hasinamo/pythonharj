class Paikka:
    """Paikka-olio sisältää paikan tiedot."""

    def __init__(self, nimi, esine=None):
        self.nimi = nimi
        self.esine = esine
        self.yhteydet = []

    def lisaa_yhteys(self, paikka):
        """Lisää paikan mahdolliseksi kulkupaikaksi."""
        self.yhteydet.append(paikka)

    def nayta_tiedot(self):
        """Näyttää nykyisen paikan tiedot."""

        print()
        print("=== PAIKAN TIEDOT ===")
        print("Paikka:", self.nimi)

        if self.esine is None:
            print("Täällä ei ole esinettä.")

        else:
            print("Täällä on:", self.esine.nimi)

        if len(self.yhteydet) == 0:
            print("Tästä ei ole muita reittejä.")

        else:
            print("Tästä voit mennä:")

            for paikka in self.yhteydet:
                print("-", paikka.nimi)