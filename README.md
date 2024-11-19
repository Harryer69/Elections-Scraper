# Elections Scraper 
Třetí projek do Engeto Python Akademie

## Popis projektu
Cílem tohoto projektu je napsat kód pro extrakci parlamentních voleb z roku 2017 z tohoto odkazu: https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

## Knihovny
Knihovny použité v tomto programu jsou uvedeny v souboru: requirements.txt

## Spuštění programu
Program se spouští pomocí dvou argumentů. python Scraper.py <odkaz_uzemniho_celku> <vystupni_soubor>. Jako výstupní soubor program vytvoří soubor csv.

## Ukázka
Pro spuštení programu musím zadat skrze terminál správnou cestu k souboru Scraper.py. Následně vložím první argument (odkaz: musí být v uvozovkách) a druhý argument který pojmenuje výstupní csv soubor (také v uvozovkách).

### Spuštení programu

Argument_1 - "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7105"  

Argument_2 - "Sumperk_volby.csv

### Průběh programu
 
Stahuji data z URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7105
Stahuji data z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec=525588&xvyber=7105
Stahuji data z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec=525804&xvyber=7105
Stahuji data z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec=525880&xvyber=7105
Stahuji data z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec=525979&xvyber=7105
Stahuji data z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec=526169&xvyber=7105
Stahuji data z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec=569437&xvyber=7105  

Ukládám data do souboru Sumperk_volby.csv

Po skončení běhu programu se vytvoří csv soubor, který obsahuje výsledky parlamentních voleb ze zadaného okresu pomocí odkazu.




