# ===== Uued harjutusülesanded =====

# 1. Pesastatud listidest esimese elemendi eraldamine
# Tagasta uus list, mis koosneb iga sisendiks antud alamlisti esimesest elemendist.
def esimesed_elemendid(pesastatud_listid):
    tulemus = []
    for alamlist in pesastatud_listid:
        tulemus.append(alamlist[0])
    # Kirjuta siia implementatsioon
    return tulemus


print(esimesed_elemendid([[1, 2, 3], [4, 5], [6, 7, 8, 9]]))  # expected output: [1, 4, 6]


# 2. Positiivsed arvud listist
# Tagasta uus list, kuhu kuuluvad ainult positiivsed arvud (rangelt suuremad kui null).
def positiivsed_arvud(arvud):
    tulemus = []
    for posi in arvud:
        if posi > 0:
            tulemus.append(posi)
    # Kirjuta siia implementatsioon
    return tulemus


print(positiivsed_arvud([-9, 8, -7, 1, -2, 3, 0]))  # expected output: [8, 1, 3]


# 3. Listi elementide summa (ilma sum() funktsioonita)
# Käi list for-tsükliga läbi ja leia kõikide arvude summa.
def leia_summa(arvud):
    summa = 0
    for arv in arvud:
        summa += arv
    # Kirjuta siia implementatsioon
    return summa


print(leia_summa([3, 17, -5, 9, 12]))  # expected output: 36


# 4. Kaashäälikute loendamine sõnes
# Loenda, mitu kaashäälikut sõnes on. Eira täishäälikuid, tühikuid ja muid märke.
# Suur- ja väiketähti kohtle ühtemoodi.
def kaashaalikud(sone):
    taishaalikud = "aeiouõäöü"
    loendur = 0
    for taht in sone.lower():
        if taht.isalpha() and taht not in taishaalikud:
            loendur += 1
    
    # Kirjuta siia implementatsioon
    return loendur


print(kaashaalikud("Kalevipoeg"))  # expected output: 5
print(kaashaalikud("Kaval Ants"))  # expected output: 5


# 5. Tähtede esinemissageduse loendamine sõnastikku
# Tagasta sõnastik, kus võti on täht ja väärtus on selle tähe esinemiste arv antud sõnes.
# Ignoreeri tühikuid ja muuda kõik tähed enne loendamist väiketähtedeks.
def loenda_tahed(sone):
    tulemus = {}
    for taht in sone.lower():
        if taht == " ":
            continue
        if taht in tulemus:
            tulemus[taht] += 1
        else:
            tulemus[taht] = 1
            
    # Kirjuta siia implementatsioon
    return tulemus


print(loenda_tahed("Kaval ants"))
# expected output: {'k': 1, 'a': 3, 'v': 1, 'l': 1, 'n': 1, 't': 1, 's': 1}