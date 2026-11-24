# ===== EKSAMIÜLESANNE: Õpilaste keskmised hinded =====
#
# Failis hinded.txt on igal real üks hinne kujul:
#     nimi, aine, hinne
# Näide:
#     Mari, Matemaatika, 5
#     Jüri, Matemaatika, 3


# 1. Faili lugemine
# Loe fail ja tagasta list, kus iga element on tuple (nimi, aine, hinne).
# Hinne peab olema täisarv (int).
# Vihje: with open(..., encoding="utf-8"), strip(), split(",")
def loe_hinded(failinimi):
    hinded = []
    # Kirjuta siia implementatsioon
    return hinded


hinded = loe_hinded("hinded.txt")
print(hinded[:2])
# expected output: [('Mari', 'Matemaatika', 5), ('Jüri', 'Matemaatika', 3)]


# 2. Keskmised hinded
# Tagasta sõnastik, kus võti on õpilase nimi ja väärtus on tema
# hinnete keskmine, ümardatud kahe komakohani.
# Vihje: kogu sõnastikku iga õpilase hinnete summa ja hinnete arv, round(..., 2)
def keskmised(hinded):
    tulemus = {}
    # Kirjuta siia implementatsioon
    return tulemus


k = keskmised(hinded)
print(k)
# expected output: {'Mari': 4.67, 'Jüri': 3.0, 'Kati': 4.0}


# 3. Pingerida
# Prindi õpilased keskmise hinde järgi kahanevas järjekorras (parim esimesena)
# kujul   Nimi: keskmine
# Vihje: sorted(..., key=..., reverse=True), .items()
def prindi_pingerida(keskmised_dict):
    # Kirjuta siia implementatsioon
    pass


prindi_pingerida(k)
# expected output:
# Mari: 4.67
# Kati: 4.0
# Jüri: 3.0


# 4. LISAÜLESANNE (kui aega jääb): parim aines
# Tagasta selle õpilase nimi, kellel on antud aines kõrgeim hinne.
def parim_aines(hinded, aine):
    # Kirjuta siia implementatsioon
    return None


print(parim_aines(hinded, "Matemaatika"))  # expected output: Mari
