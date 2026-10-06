class pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.sijainti = sijainti
        self.inventaario = []

    def liiku(self, uusi_paikka):
        self.sijainti = uusi_paikka
        print("Siirryit paikkaan:", uusi_paikka.nimi)

    def keraa_esine(self):
        if self.sijainti.esine is None:
            print("Tässä paikassa ei ole esinettä.")
        else:
            esine = self.sijainti.esine
            self.inventaario.append(esine)
            self.sijainti.esine = None
            print("Keräsit:", esine.nimi)

    def nayta_inventaario(self):
        print("=== INVENTAARIO ===")

        if len(self.inventaario) == 0:
            print("Tyhjä.")
        else:
            for esine in self.inventaario:
                print("-", esine.nimi)