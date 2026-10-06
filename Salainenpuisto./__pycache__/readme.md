# Salainen puisto

## Pelin idea

Salainen puisto on komentorivillä toimiva
tekstiseikkailupeli.

Pelaaja on puiston portilla ja huomaa,
että hänen avaimensa on kadonnut.

Pelaajan tehtävä on löytää Avain
ja palata sen kanssa takaisin Portille.

## Pelaaja

Peli kysyy pelaajan iän ja nimen.

Alle 12-vuotias ei voi pelata peliä.

Pelaajalla on seuraavat tiedot:

- nimi
- ikä
- sijainti
- inventaario
- pisteet

## Päävalikko

Pelissä on seuraavat komennot:

- pelaa
- pisteet
- ohje
- liiku
- kerää
- inventaario
- paikka
- tallenna
- lataa
- lopeta

## Paikat

Pelissä on viisi paikkaa:

- Portti
- Puisto
- Kirjasto
- Pyöräasema
- Lampi

Paikoilla on yhteyksiä toisiin paikkoihin.
Tämän avulla pelaajalle muodostuu kolme erilaista
reittiä.

## Kolme reittiä

Ensimmäinen reitti:

Portti -> Puisto -> Lampi -> Portti

Toinen reitti:

Portti -> Kirjasto -> Puisto -> Lampi -> Portti

Kolmas reitti:

Portti -> Pyöräasema -> Lampi -> Portti

Peli ei anna pelaajan siirtyä paikkaan,
johon nykyisestä paikasta ei ole yhteyttä.

## Esineet

Pelissä on kolme esinettä:

- Avain
- Vesipullo
- Kirja

Avain on pelin tärkein esine.

Kun pelaaja kerää esineen,
se siirtyy inventaarioon.

## Pisteet

Pelaaja aloittaa 100 pisteellä.

Jokaisesta kerätystä esineestä saa 10 pistettä.

## Tiedostot

intro.txt sisältää pelin aloitustekstin.

ohjeet.txt sisältää pelin ohjeet.

tallennus.txt luodaan automaattisesti,
kun pelaaja käyttää tallenna-komentoa.

## Luokat

Pelissä on kolme luokkaa:

- Pelaaja
- Paikka
- Esine

Pelaaja-luokka sisältää pelaajan tiedot.

Paikka-luokka sisältää paikan tiedot,
esineen ja mahdolliset yhteydet.

Esine-luokka sisältää esineen nimen ja painon.

## Funktiot

Pääohjelmassa käytetään useita funktioita,
esimerkiksi:

- lue_tiedosto
- hae_paikka
- liiku
- tallenna_peli
- lataa_peli
- tarkista_voitto
- nayta_pisteet
- luo_peli
- kaynnista_peli

Funktioiden avulla ohjelma on helpompi
jakaa pienempiin osiin.

## Ohjelmointiasiat

Projektissa käytetään:

- muuttujia
- if-rakenteita
- while-silmukkaa
- for-silmukoita
- funktioita
- parametreja
- return-arvoja
- listoja
- luokkia
- olioita
- tiedostojen lukemista
- tiedostojen kirjoittamista

## Kestävä kehitys

Pelin aihe liittyy kestävään kehitykseen.

Pelissä on puisto, kirjasto ja pyöräasema.
Pelaaja voi käyttää kävelyyn ja pyöräilyyn
liittyvää teemaa.

Kävely ja pyöräily ovat ympäristöystävällisiä
liikkumistapoja.

Aihe liittyy YK:n kestävän kehityksen tavoitteeseen
11: Kestävät kaupungit ja yhteisöt.

## Voittaminen

Pelaaja voittaa, kun hän:

1. löytää Avaimen
2. kerää Avaimen
3. palaa Portille

Sen jälkeen peli ilmoittaa voitosta
ja näyttää pelaajan pisteet.

## Kehitys

Peli perustuu aikaisempiin projekteihin.

Projektissa 2 tehtiin ikätarkistus
ja päävalikko.

Projektissa 3 tehtiin funktioita
ja inventaario.

Projektissa 4 lisättiin luokat ja oliot.

Projektissa 5 lisättiin tiedostojen lukeminen
ja tallentaminen.

Lopullisessa projektissa nämä asiat
on yhdistetty yhdeksi peliksi.