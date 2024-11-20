# Elections Scraper 
Třetí projek do Engeto Python Akademie

## Popis projektu
Cílem tohoto projektu je napsat kód pro extrakci parlamentních voleb z roku 2017 z tohoto odkazu: https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

## Knihovny
Knihovny použité v tomto programu jsou uvedeny v souboru: requirements.txt  

Instalace knihoven se spouští pomocí příkazu v termínálu:

pip install reuquirements.txt

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

Ukončuji ....... Scraper.py


Po skončení běhu programu se vytvoří csv soubor, který obsahuje výsledky parlamentních voleb ze zadaného okresu pomocí odkazu.

## Částečný výstup
Kód obce,Název obce,Voliči,Vydané obálky,Platné hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická  str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů  

525588,Bludov,2 504,1 632,1 615,"11,02%","0,00%","0,00%","7,61%","0,06%","8,23%","6,93%","1,17%","1,05%","0,61%","0,06%","0,00%","6,81%","0,18%","2,35%","31,76%","0,06%","0,00%","8,42%","0,00%","0,18%","0,18%","0,12%","12,87%","0,24%",-%  

525804,Bohdíkov,1 103,640,634,"5,20%","0,31%","0,31%","6,62%","0,00%","6,30%","10,09%","0,94%","1,10%","0,78%","0,31%","0,00%","6,94%","0,00%","1,73%","35,80%","0,00%","0,15%","5,67%","0,00%","0,00%","0,00%","0,00%","17,35%","0,31%",-%
525880,Bohuslavice,413,269,267,"2,99%","0,00%","0,00%","6,74%","0,00%","4,49%","9,73%","0,37%","0,37%","2,99%","0,37%","0,00%","6,74%","0,00%","1,49%","37,82%","0,00%","0,00%","13,85%","0,00%","0,37%","0,37%","0,00%","11,23%","0,00%",-%  

525979,Bohutín,609,379,373,"6,16%","0,00%","0,00%","5,89%","0,00%","5,36%","13,94%","0,80%","0,00%","1,87%","0,26%","0,00%","6,16%","0,00%","0,53%","32,70%","0,00%","0,26%","9,91%","0,26%","0,00%","0,26%","0,00%","15,28%","0,26%",-%





