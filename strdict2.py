# H1. Täishäälikute loendamine
# Tagasta, mitu täishäälikut (a, e, i, o, u, õ, ä, ö, ü) on sõnes.
# Suured ja väikesed tähed loevad mõlemad.
# Vihje: .lower() teeb kõik tähed väikeseks; "a" in "aeiou" annab True.
def loenda_taishaalikud(sone):
    vokaalid = "aeiouõäöü"
    count = 0
    for taht in sone:
        if taht in vokaalid:
            count += 1
    # Kirjuta siia implementatsioon
    return count


print(loenda_taishaalikud("Programmeerimine"))  # expected output: 7
print(loenda_taishaalikud("Tere"))  # expected output: 2


# H2. Lühim sõna lauses
# Tagasta lause kõige lühem sõna. Kui mitu sõna on sama lühikesed, tagasta esimene.
# Vihje: sarnane E6-ga, aga algväärtuseks sobib lause esimene sõna.
def luhim_sona(lause):
    luhim = lause.split()[0]
    for sona in lause.split():
        if len(sona) < len(luhim):
            luhim = sona
    
    # Kirjuta siia implementatsioon
    return luhim


print(luhim_sona("Python on väga lahe keel"))  # expected output: on
print(luhim_sona("Kass ja koer"))  # expected output: ja


# H3. Paarisarvude summa
# Tagasta listi kõigi paarisarvude summa.
# Vihje: arv on paaris, kui arv % 2 == 0.
def paaris_summa(arvud):
    summa = 0
    for arv in arvud:
        if arv % 2 == 0:
            summa += arv
    # Kirjuta siia implementatsioon
    return summa


print(paaris_summa([1, 2, 3, 4, 5, 6]))  # expected output: 12
print(paaris_summa([7, 9, 11]))  # expected output: 0


# H4. Parim õpilane
# Sõnastikus on võtmeks õpilase nimi ja väärtuseks hinne.
# Tagasta kõrgeima hindega õpilase nimi. Kui mitu on võrdsed, tagasta esimene.
# Vihje: kombineeri E6 (seni parima meelespidamine) ja E9 (sõnastiku läbimine).
def parim_opilane(hinded):
    parim_nimi = ""
    parim_hinne = 0
    for nimi in hinded:
        if hinded[nimi] > parim_hinne:
            parim_nimi=nimi
            parim_hinne=hinded[nimi]
    return parim_nimi
    # Kirjuta siia implementatsioon
    


print(parim_opilane({"Mari": 4, "Jüri": 5, "Kati": 3}))  # expected output: Jüri
print(parim_opilane({"Ats": 5, "Pille": 5}))  # expected output: Ats


# H5. Sõnade loendamine sõnastikku
# Tagasta sõnastik, kus võti on sõna ja väärtus on selle sõna esinemiste arv lauses.
# Vihje: sama nagu E8, aga tähtede asemel käi läbi lause.split().
def loenda_sonad(lause):
    d = {}
    for sona in lause.split():
        if sona in d:
            d[sona]+=1
        else:
            d[sona]=1
            
    # Kirjuta siia implementatsioon
    return d


print(loenda_sonad("kass koer kass hiir kass"))  # expected output: {'kass': 3, 'koer': 1, 'hiir': 1}
print(loenda_sonad("tere tere"))  # expected output: {'tere': 2}


# H6. Positiivse hindega õpilased
# Sõnastikus on võtmeks nimi ja väärtuseks hinne.
# Tagasta list nendest nimedest, kelle hinne on vähemalt 3.
# Vihje: alusta tühja listiga [] ja lisa nimesid .append() abil.
def labisid(hinded):
    tulemus = []
    for nimi in hinded:
        if hinded[nimi] >= 3:
            tulemus.append(nimi)
    # Kirjuta siia implementatsioon
    return tulemus


print(labisid({"Mari": 5, "Jüri": 2, "Kati": 3}))  # expected output: ['Mari', 'Kati']
print(labisid({"Ats": 1, "Pille": 2}))  # expected output: []


# H7. Sõne tagurpidi ilma [::-1]-ta
# Tagasta sõne tagurpidi. Ära kasuta lõikamist [::-1].
# Vihje: alusta tühja sõnega "" ja lisa iga täht ETTE: uus = taht + uus.
def tagurpidi(sone):
    sona = ""
    for taht in sone:
        sona = taht + sona
    # Kirjuta siia implementatsioon
    return sona


print(tagurpidi("kass"))  # expected output: ssak
print(tagurpidi("Python"))  # expected output: nohtyP


# H8. Kõige sagedasem täht
# Tagasta täht, mis esineb sõnes kõige rohkem kordi. Tühikuid ära loenda.
# Kui mitu tähte on võrdselt sagedased, tagasta see, mis esineb sõnes esimesena.
# Vihje: kõigepealt loenda tähed nagu E8-s, siis leia suurim nagu H4-s.
def sagedasim_taht(sone):
    d = {}
    for taht in sone:
        if taht in d:
            d[taht]+=1
        else:
            d[taht]=1
    parim_taht = ""
    parim_arv = 0
    for taht in d:
        if d[taht] > parim_arv:
            parim_taht = taht
            parim_arv = d[taht]
    return parim_taht
    # Kirjuta siia implementatsioon
    


print(sagedasim_taht("banaan"))  # expected output: a
print(sagedasim_taht("aa bb"))  # expected output: a