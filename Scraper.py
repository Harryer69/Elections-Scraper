"""projekt_3.1.py: třetí projekt do Engeto Online Python Akademie
author: Tomáš Rossmanith
email: rossmanith.tomas@gmail.com
discord: tomasrossmanith
"""

import sys
import csv
import requests
import bs4

volici = []
ucast = []
platne = []

def adresa(odkaz):
    """ Tato funkce stáhne HTML obsah a vrátí objekt BeautifulSoup """
    obsah_url = requests.get(odkaz)
    html = bs4.BeautifulSoup(obsah_url.text, "html.parser")
    print("Stahuji data z URL:", odkaz)
    return html

if len(sys.argv) == 3:
    opakovana_html = adresa(sys.argv[1])  # ulození HTML pro opakované použití
else:
    print("Zadal jsi nesprávný počet argumentů. Argumenty musí být 3. Název souboru, URL adresa v uvozovkách a název csv souboru")
    quit()

def mesta():
    """ Vrací seznam měst """
    mesto = []
    hledani_mest = opakovana_html.find_all("td", "overflow_name")
    for m in hledani_mest:
        mesto.append(m.text)
    return mesto

def URL():
    """ Vrací URL adresu k získání detailů obcí v okrese """
    cesta_URL = []
    hledej_odkaz = opakovana_html.find_all("td", class_="cislo")
    for odkaz_mesta in hledej_odkaz:
        odkaz_mesta = odkaz_mesta.a["href"]
        cesta_URL.append(f"https://volby.cz/pls/ps2017nss/{odkaz_mesta}")
    return cesta_URL

def id():
    """ Vrací ID čísla obcí """
    id_mesta = []
    hledej_id = opakovana_html.find_all("td", class_="cislo")
    for i in hledej_id:
        id_mesta.append(i.text)
    return id_mesta

def kandidujici_strany():
    """ Vrací seznam kandidujících stran v okrese """
    strany = []
    mesta_odkazy = URL()
    html = requests.get(mesta_odkazy[0])
    html_obce = bs4.BeautifulSoup(html.text, "html.parser")
    strana = html_obce.find_all("td", "overflow_name")
    for s in strana:
        strany.append(s.text)
    return strany

def pocty_volicu():
    """ Jde o modifikační funkci, která do proměnných volic, účasti, správná účast přidá celkový počet registrovaných
    voličů, zúčastněných voličů a platných hlasů v jednotlivých obcích"""
    cesta_k_odkazu = URL()
    for c in cesta_k_odkazu:
        html_cesta = requests.get(c)
        obce_html = bs4.BeautifulSoup(html_cesta.text, "html.parser")
        volic = obce_html.find_all("td", headers="sa2")
        for v in volic:
            volici.append(v.text.replace("\xa0", " "))
        ucasti = obce_html.find_all("td", headers="sa3")
        for u in ucasti:
            ucast.append(u.text.replace("\xa0", " "))
        spravna_ucast = obce_html.find_all("td", headers="sa6")
        for s in spravna_ucast:
            platne.append(s.text.replace("\xa0", " "))

def volebni_hlasy():
    """ Funkce vrací list listů, kde jsou seřazeny procentuální výsledky politických stran v jednotlivých obcích """
    odkaz = URL()
    hlasy_volicu = []
    for o in odkaz:
        html = adresa(o)
        vyhledvani_hlasu = html.find_all("td", headers=["t1sb4", "t2sb4"])
        temp = []
        for v in vyhledvani_hlasu:
            temp.append(v.text + "%")
        hlasy_volicu.append(temp)
    return hlasy_volicu

def pomocna_csv():
    """ Pomocná funkce pro tvorbu csv souborů. Tato fce vrací list listů. Vytvoří csv kde je ID konkrétní obce,
    název, reg. voliči, zúčastnění voliči, platné hlasy a výsledky každé z kandidujících stran """
    radky = []
    pocty_volicu()
    mesta_obce = mesta()
    ids = id()
    hlasy = volebni_hlasy()
    zipped = zip(ids, mesta_obce, volici, ucast, platne)
    pomocna_promenna = []
    for i, m, v, u, p in zipped:
        pomocna_promenna.append([i, m, v, u, p])
    zip_vse = zip(pomocna_promenna, hlasy)
    for pp, hl in zip_vse:
        radky.append(pp + hl)
    return radky

def volby(link, slozka):
    """ Funkce, která s funkcemi výše vytvoří csv soubor s výsledky voleb"""
    try:
        zahlavi = ["Kód obce", "Název obce", "Voliči", "Vydané obálky", "Platné hlasy"]
        obsah = pomocna_csv()
        strany = kandidujici_strany()
        print("Ukládám data do souboru", slozka)
        for strana in strany:
            zahlavi.append(strana)
        with open(slozka, "w", newline="", encoding="utf-8") as f:
            f_writer = csv.writer(f)
            f_writer.writerow(zahlavi)
            f_writer.writerows(obsah)
        print("Ukončuji", sys.argv[0])
    except IndexError:
        print("Chyba. Pravděpodobně jste zapomněli napsat uvozovky nebo vložili špatný odkaz")
        quit()

if __name__ == "__main__":
    adresy = sys.argv[1]
    jmeno_slozky = sys.argv[2]
    volby(adresy, jmeno_slozky)