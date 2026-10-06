# Tuntiharjoituksia 26.8.2026
# https://github.com/ilkkamtk/python-tuntiesimerkit#moduuli-3---valintarakenne-if

# Sähkölaskulaskin

kulutus = float(input("\n Syötä sähkönkulutus (kWh): ")) 

hinta = 0 

if kulutus <= 50:
    # kW/h hinta on aina 10 senttiä
    hinta = kulutus * 10 
elif kulutus <= 200:
    # ensimmäiset 50 kW/h 10 senttiä 
    hinta = 50 * 10
    # ja loput 8 senttiä
    hinta += (kulutus - 50) * 8
else:
    # ensimmäiset kW/h 10 senttiä, seuraavat 150 8 senttiä
    # loput yli 200 kW/h 6 senttiä
     hinta = 50 * 10 + 150 * 8 + (kulutus - 200) * 6

# Tulostuksen hifistely kotimaiseen muotoon
print(f"Sähköön hinta: {hinta//100:.0f}, {hinta%100:.0f} senttiä.") 


