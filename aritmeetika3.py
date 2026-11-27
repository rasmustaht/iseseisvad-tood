# ===== Aritmeetika: harjutus 4 =====


# D1. Kuubi ruumala ja pindala
# Antud on kuubi serva pikkus a. Tagasta list [ruumala, täispindala].
# Valemid: ruumala = a³, täispindala = 6 * a²
def kuup(a):
    ruumala = a**3
    täispindala = 6*a**2
    # Kirjuta siia implementatsioon
    return [ruumala, täispindala]


print(kuup(3))  # expected output: [27, 54]
print(kuup(1.5))  # expected output: [3.375, 13.5]


# D2. Kolmekohalise arvu numbrite summa
# Antud on kolmekohaline täisarv. Tagasta tema numbrite summa.
# Näide: 365 -> 3 + 6 + 5 = 14
# Vihje: sajalised n // 100, ühelised n % 10. Kuidas saada keskmine number?
def numbrite_summa3(n):
    esimene = (n//100)
    teine = (n%100)//10
    kolmas = n%10
    keskmine =(esimene+teine+kolmas)
    # Kirjuta siia implementatsioon
    return keskmine


print(numbrite_summa3(365))  # expected output: 14
print(numbrite_summa3(909))  # expected output: 18


# D3. Paaris arv
# Tagasta True, kui arv on paaris, ja False, kui paaritu.
# Vihje: paarisarvu jagamisel 2-ga on jääk 0. Võrdlus ise annab True/False.
def on_paaris(n):
    if n % 2 == 0:
        return True
    else:
        return False
    # Kirjuta siia implementatsioon
    return n


print(on_paaris(10))  # expected output: True
print(on_paaris(7))  # expected output: False


# D4. Kütusekulu
# Antud on kulunud liitrid ja sõidetud kilomeetrid.
# Tagasta kütusekulu liitrites 100 km kohta, ümardatud ühe komakohani.
def kytusekulu(liitrid, km):
    kmliitriga = liitrid/km
    kulu = kmliitriga*100
    # Kirjuta siia implementatsioon
    return round(kulu,1)


print(kytusekulu(45, 600))  # expected output: 7.5
print(kytusekulu(66, 550))  # expected output: 12.0


# D5. Päevad -> nädalad ja päevad
# Tagasta sõne kujul "x näd y p".
# Vihje: // , % ja f-string
def nadalad(paevad):
    nadal=paevad//7
    paev=paevad%7
    # Kirjuta siia implementatsioon
    return(f'{nadal} näd {paev} p')


print(nadalad(17))  # expected output: 2 näd 3 p
print(nadalad(6))  # expected output: 0 näd 6 p


# D6. Käibemaks
# Antud on hind ilma käibemaksuta. Käibemaks on 24%.
# Tagasta list [käibemaksu summa, hind koos käibemaksuga], mõlemad ümardatud kahe komakohani.
def kaibemaks(hind):
    kmtegur = 0.24
    km = kmtegur*hind
    lopphind = hind + km
    # Kirjuta siia implementatsioon
    return [round(km,2),round(lopphind,2)]


print(kaibemaks(100))  # expected output: [24.0, 124.0]
print(kaibemaks(9.99))  # expected output: [2.4, 12.39]


# D7. Tüübiteisendus ja sõne
# Parameetrid on täisarvud sõnena (nagu input() tagastab).
# Tagasta sõne kujul "a + b = summa".
# Vihje: sõnesse panemiseks pole teisendust vaja, liitmiseks on.
def liitmistehe(a, b):
    summa = int(a)+int(b)
    # Kirjuta siia implementatsioon
    return f'{a} + {b} = {summa}'


print(liitmistehe("5", "3"))  # expected output: 5 + 3 = 8
print(liitmistehe("12", "30"))  # expected output: 12 + 30 = 42