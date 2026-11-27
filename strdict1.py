# Harjutus - listid, sõned, tingimuslaused, sõnastikud
# Igas ülesandes on funktsiooni toorik. Kirjuta implementatsioon ja käivita fail,
# et kontrollida, kas väljund vastab kommentaaris olevale oodatavale tulemusele.
# NB! Kasuta funktsiooni sees alati parameetrit, mitte funktsioonist väljas olevat muutujat.


# ===== Listid =====


# E1. Pesastatud listi kõigi arvude summa
# Käi pesastatud list kahe for-tsükliga läbi ja liida kõik arvud kokku (ilma sum() funktsioonita).
def pesastatud_summa(nested):
    kokku = 0
    for väljas in nested:
        for sees in väljas:
            kokku += sees
    # Kirjuta siia implementatsioon
    return kokku


print(pesastatud_summa([[1, 2], [3, 4, 5], [10]]))  # expected output: 25


# E2. Negatiivsete arvude eemaldamine
# Tagasta uus list, kuhu kuuluvad ainult arvud, mis on suuremad või võrdsed nulliga.
def mitte_negatiivsed(arvud):
    tulemus = []
    for neg in arvud:
        if neg >= 0:
            tulemus.append(neg)
            
    
    # Kirjuta siia implementatsioon
    return tulemus


print(mitte_negatiivsed([3, -1, 0, -7, 5]))  # expected output: [3, 0, 5]


# E3. Väikseim arv listist (ilma min() funktsioonita)
# Käi list for-tsükliga läbi ja leia väikseim element.
def vaikseim(arvud):
    väikseim = arvud[0]
    for i in arvud:
        if i < väikseim:
            väikseim=i
        
    # Kirjuta siia implementatsioon
    return väikseim


print(vaikseim([8, 3, -2, 10]))  # expected output: -2
print(vaikseim([5]))  # expected output: 5


# ===== Sõned =====


# E4. Suurtähtede loendamine
# Loenda, mitu suurtähte sõnes on.
# Vihje: sõnemeetod .isupper() tagastab True, kui täht on suurtäht.
def suurtahed(sone):
    count = 0
    for i in sone:
        if i.isupper():
         count += 1
    # Kirjuta siia implementatsioon
    return count


print(suurtahed("Tere Tallinn ja Tartu"))  # expected output: 3
print(suurtahed("Õhtu Ülemistes"))  # expected output: 2


# E5. Sõne tagurpidi (ilma [::-1] kasutamata)
# Käi sõne for-tsükliga läbi ja ehita uus sõne, kus tähed on vastupidises järjekorras.
# Vihje: alusta tühja sõnega "" ja lisa iga täht olemasoleva sõne ETTE.
def tagurpidi(sone):
    sona = ""
    for i in sone:
        sona = i + sona
        
    
    # Kirjuta siia implementatsioon
    return sona


print(tagurpidi("Python"))  # expected output: nohtyP
print(tagurpidi("kirik"))  # expected output: kirik


# E6. Pikim sõna lauses
# Tagasta lause kõige pikem sõna. Kui mitu sõna on sama pikad, tagasta esimene neist.
# Vihje: .split() teeb lausest sõnade listi.
def pikim_sona(lause):
    pikim = ""
    for sona in lause.split():
        if len(sona) > len(pikim):
            pikim = sona
    # Kirjuta siia implementatsioon
    return pikim


print(pikim_sona("Programmeerimine on tore"))  # expected output: Programmeerimine
print(pikim_sona("Kass ja koer"))  # expected output: Kass


# ===== Tingimuslaused =====


# E7. Punktid -> hinne
# 91-100 -> 5, 81-90 -> 4, 71-80 -> 3, 61-70 -> 2, 51-60 -> 1, alla 51 -> 0
# Vihje: if / elif / else. Mõtle, mis järjekorras tingimusi kontrollida.
def hinne(punktid):
    if punktid >= 91:
        return 5
    elif punktid >= 81:
        return 4
    elif punktid >= 71:
        return 3
    elif punktid >= 61:
        return 2
    elif punktid >= 51:
        return 1
    else:
        return 0
    # Kirjuta siia implementatsioon



print(hinne(95))  # expected output: 5
print(hinne(81))  # expected output: 4
print(hinne(50))  # expected output: 0


# ===== Sõnastikud =====


# E8. Tähtede esinemiste loendamine sõnastikku
# Tagasta sõnastik, kus võti on täht ja väärtus on selle tähe esinemiste arv sõnes.
# Tühikuid ära loenda.
def loenda_tahed(sone):
    d = {}
    for taht in sone:
        if taht == " ":
            continue
        if taht in d:
            d[taht]+=1
        else:
            d[taht]=1
            
            
    # Kirjuta siia implementatsioon
    return d


print(loenda_tahed("banaan"))  # expected output: {'b': 1, 'a': 3, 'n': 2}
print(loenda_tahed("aa bb a"))  # expected output: {'a': 3, 'b': 2}


# E9. Hinnete keskmine sõnastikust
# Sõnastikus on võtmeks õpilase nimi ja väärtuseks hinne.
# Tagasta hinnete keskmine, ümardatud kahe komakohani.
# Vihje: for nimi in hinded: ... annab võtmed; hinded[nimi] annab väärtuse. len() töötab ka sõnastikuga.
def keskmine_hinne(hinded):
    summa = 0
    for nimi in hinded:
        summa += hinded[nimi]
    keskmine = summa/len(hinded)
    
    # Kirjuta siia implementatsioon
    return keskmine


print(keskmine_hinne({"Mari": 5, "Jüri": 3, "Kati": 4}))  # expected output: 4.0
print(keskmine_hinne({"Ats": 5, "Pille": 4}))  # expected output: 4.5