class Esine:
    """Esine-olio sisältää esineen tiedot."""

    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino

    def nayta_tiedot(self):
        """Näyttää esineen tiedot."""

        print("Esine:", self.nimi)
        print("Paino:", self.paino, "kg")