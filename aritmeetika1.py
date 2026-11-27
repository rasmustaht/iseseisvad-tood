# ===== Aritmeetika: harjutus 2 =====
import math


# B1. Ringi pindala ja ümbermõõt
# Tagasta list [pindala, ümbermõõt], mõlemad ümardatud kahe komakohani.
# Valemid: pindala = pi * r², ümbermõõt = 2 * pi * r
# Vihje: math.pi , ** , round()
def ring(r):
    
    pindala = math.pi * r ** 2
    ümbermõõt = 2 * math.pi * r
    # Kirjuta siia implementatsioon
    return [round(pindala, 2), round(ümbermõõt, 2)]


print(ring(3))  # expected output: [28.27, 18.85]
print(ring(1))  # expected output: [3.14, 6.28]


# B2. Tulemus protsentides
# Tagasta, mitu protsenti maksimumpunktidest saadi. Ümarda ühe komakohani.
def protsent(punktid, max_punktid):
    osa = punktid/max_punktid
    protsendid = round((osa*100), 1)
    
    
    # Kirjuta siia implementatsioon
    return protsendid


print(protsent(37, 50))  # expected output: 74.0
print(protsent(2, 3))  # expected output: 66.7


# B3. Sendid -> eurod ja sendid
# Tagasta list [eurod, sendid].
# Vihje: // , %
def raha(sendid):
    eurod = sendid // 100
    mündid = sendid % 100
    # Kirjuta siia implementatsioon
    return [eurod, mündid]


print(raha(1275))  # expected output: [12, 75]
print(raha(99))  # expected output: [0, 99]


# B4. Kilomeetrid -> miilid
# Valem: miilid = km / 1.609. Ümarda tulemus kahe komakohani.
def km_miilid(km):
    miilid = km/1.609
    # Kirjuta siia implementatsioon
    return round(miilid, 2)


print(km_miilid(10))  # expected output: 6.22
print(km_miilid(42.195))  # expected output: 26.22


# B5. Minutid -> päevad, tunnid, minutid
# Tagasta sõne kujul "d p hh:mm", st tunnid ja minutid alati kahekohalised.
# Ühes päevas on 1440 minutit.
# Vihje: // , % ja f-string vormindus {t:02d}
def minutid(m):
    päev = m // 1440
    tunnid = (m%1440)//60
    minutid = m%60
    # Kirjuta siia implementatsioon
    return (f'{päev} p {tunnid:02d}:{minutid:02d}')


print(minutid(1505))  # expected output: 1 p 01:05
print(minutid(75))  # expected output: 0 p 01:15


# B6. Tüübiteisendus
# Parameetrid on sõned (nagu input() tagastab): hind komakohtadega ja kogus täisarvuna.
# Tagasta koguhind ujukomaarvuna, ümardatud kahe komakohani.
def koguhind(hind, kogus):
    kokku = float(hind) * int(kogus)
    # Kirjuta siia implementatsioon
    return float(round(kokku, 2))


print(koguhind("12.50", "3"))  # expected output: 37.5
print(koguhind("0.99", "4"))  # expected output: 3.96