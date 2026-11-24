'''
EKSAMIÜLESANNE: Õpilaste keskmised hinded

Failis hinded.txt on igal real üks hinne kujul:
    nimi, aine, hinne

Näide:
    Mari, Matemaatika, 5
    Jüri, Matemaatika, 3

Kirjuta kolm funktsiooni:

1. loe_hinded(failinimi)
   Loeb faili ja tagastab listi, kus iga element on tuple (nimi, aine, hinne).
   Hinne peab olema täisarv (int).

2. keskmised(hinded)
   Tagastab sõnastiku, kus võti on õpilase nimi ja väärtus on tema
   hinnete keskmine, ümardatud kahe komakohani.

3. prindi_pingerida(keskmised_dict)
   Prindib õpilased keskmise hinde järgi kahanevas järjekorras
   (parim esimesena) kujul:   Nimi: keskmine

Oodatav väljund:
    Mari: 4.67
    Kati: 4.0
    Jüri: 3.0

Lisaülesanne (kui aega jääb):
4. parim_aines(hinded, aine) – tagastab selle õpilase nime,
   kellel on antud aines kõrgeim hinne.
   parim_aines(hinded, "Matemaatika")  ->  'Mari'
'''


def loe_hinded(failinimi):
    hinded = []
    # Kirjuta siia implementatsioon
    return hinded


def keskmised(hinded):
    tulemus = {}
    # Kirjuta siia implementatsioon
    return tulemus


def prindi_pingerida(keskmised_dict):
    # Kirjuta siia implementatsioon
    pass


hinded = loe_hinded("hinded.txt")
print(hinded[:2])
# expected output: [('Mari', 'Matemaatika', 5), ('Jüri', 'Matemaatika', 3)]

k = keskmised(hinded)
print(k)
# expected output: {'Mari': 4.67, 'Jüri': 3.0, 'Kati': 4.0}

prindi_pingerida(k)
# expected output:
# Mari: 4.67
# Kati: 4.0
# Jüri: 3.0
