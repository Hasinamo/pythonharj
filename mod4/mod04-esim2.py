# Tuntiharjoituksia 26.8.2026
# https://github.com/ilkkamtk/python-tuntiesimerkit#moduuli-3---valintarakenne-if

# Sähkölaskulaskin

kulutus = float(input("\nSyötä sähkönkulutus (kWh): "))
hinta = 0

if kulutus <= 50:
    # kWh hinta on aina 10 senttiä
    hinta = kulutus * 10
elif kulutus <= 200:
    # ensimmäiset 50 kWh 10 senttiä
    hinta = 50 * 10
    # ja loput 8 senttiä
    hinta = hinta + (kulutus-50) * 8
else:
    # ensimmäiset 50 kWh 10 senttiä, seuraavat 150 8 senttiä
    # loput yli 200 kWh 6 senttiä
    hinta = 50 * 10 + 150 * 8 + (kulutus - 200) * 6

# Tulostuksen hifistely kotimaiseen muotoon
print(f"Sähkön hinta: {hinta//100:.0f},{hinta%100:.0f} euroa.") 