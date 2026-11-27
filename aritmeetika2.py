# ===== Aritmeetika: harjutus 3 =====
import math


# C1. Täisnurkse kolmnurga hüpotenuus
# Antud on kaatetid a ja b. Tagasta hüpotenuus, ümardatud kahe komakohani.
# Valem (Pythagoras): c = ruutjuur(a² + b²)
# Vihje: math.sqrt() , ** , round()
def hupotenuus(a, b):
    c = math.sqrt(a**2 + b**2)
    # Kirjuta siia implementatsioon
    return round(c,2)


print(hupotenuus(3, 4))  # expected output: 5.0
print(hupotenuus(1, 1))  # expected output: 1.41


# C2. Kehamassiindeks (KMI)
# Valem: KMI = kaal / pikkus². Kaal on kilogrammides, pikkus meetrites.
# Ümarda tulemus ühe komakohani.
def kmi(kaal, pikkus):
    massindeks = kaal / pikkus**2
    # Kirjuta siia implementatsioon
    return round(massindeks, 1)


print(kmi(70, 1.75))  # expected output: 22.9
print(kmi(90, 1.8))  # expected output: 27.8


# C3. Pitsa jagamine
# Pitsas on `viilud` viilu ja seda jagatakse `inimesed` inimese vahel võrdselt.
# Tagasta list [viile inimese kohta, üle jäänud viilud].
# Vihje: // , %
def pitsa(viilud, inimesed):
    inimenesaab = viilud//inimesed
    ylejaab = viilud % inimenesaab
    # Kirjuta siia implementatsioon
    return [inimenesaab,ylejaab]


print(pitsa(16, 3))  # expected output: [5, 1]
print(pitsa(8, 4))  # expected output: [2, 0]


# C4. Allahindlus
# Antud on hind ja allahindluse protsent. Tagasta uus hind, ümardatud kahe komakohani.
# Näide: 80 eurot, 25% soodsamalt -> 60 eurot.
def soodushind(hind, protsent):
    soodukategur = protsent/100
    soodukas = hind * soodukategur
    uushind = hind - soodukas
    # Kirjuta siia implementatsioon
    return round(uushind,2)


print(soodushind(80, 25))  # expected output: 60.0
print(soodushind(19.99, 15))  # expected output: 16.99


# C5. Keskmine kiirus
# Antud on läbitud vahemaa kilomeetrites ja aeg MINUTITES.
# Tagasta kiirus km/h, ümardatud ühe komakohani.
# Vihje: kõigepealt teisenda minutid tundideks.
def kiirus(km, minutid):
    tund = minutid / 60
    speed = km / tund
    # Kirjuta siia implementatsioon
    return round(speed, 1)


print(kiirus(10, 50))  # expected output: 12.0
print(kiirus(42.195, 215))  # expected output: 11.8


# C6. Kahekohalise arvu numbrite summa
# Antud on kahekohaline täisarv. Tagasta tema numbrite summa.
# Näide: 47 -> 4 + 7 = 11
# Vihje: kümnelised saad // abil, ühelised % abil.
def numbrite_summa(n):
    esimene = n//10
    teine = n%10
    # Kirjuta siia implementatsioon
    return(esimene+teine)


print(numbrite_summa(47))  # expected output: 11
print(numbrite_summa(90))  # expected output: 9


# C7. Tüübiteisendus
# Parameetrid on sõned (nagu input() tagastab), need võivad sisaldada komakohti.
# Tagasta kolme arvu keskmine, ümardatud kahe komakohani.
def keskmine_sonedest(a, b, c):
    kokku = float(a)+float(b)+float(c)
    keskmine = kokku/3
    # Kirjuta siia implementatsioon
    return round(keskmine,2)


print(keskmine_sonedest("4.5", "3", "5"))  # expected output: 4.17
print(keskmine_sonedest("1", "2", "2"))  # expected output: 1.67