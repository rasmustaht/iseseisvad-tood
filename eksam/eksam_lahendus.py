# LAHENDUS – eksamiülesanne "Õpilaste keskmised hinded"


def loe_hinded(failinimi):
    hinded = []
    with open(failinimi, encoding="utf-8") as f:
        for rida in f:
            if rida.strip() == "":
                continue
            osad = rida.strip().split(",")
            nimi = osad[0].strip()
            aine = osad[1].strip()
            hinne = int(osad[2].strip())
            hinded.append((nimi, aine, hinne))
    return hinded


def keskmised(hinded):
    summad = {}
    arvud = {}
    for nimi, aine, hinne in hinded:
        if nimi in summad:
            summad[nimi] += hinne
            arvud[nimi] += 1
        else:
            summad[nimi] = hinne
            arvud[nimi] = 1

    tulemus = {}
    for nimi in summad:
        tulemus[nimi] = round(summad[nimi] / arvud[nimi], 2)
    return tulemus


def prindi_pingerida(keskmised_dict):
    jarjestatud = sorted(keskmised_dict.items(), key=lambda paar: paar[1], reverse=True)
    for nimi, keskmine in jarjestatud:
        print(f"{nimi}: {keskmine}")


def parim_aines(hinded, aine):
    parim_nimi = None
    parim_hinne = -1
    for nimi, a, hinne in hinded:
        if a == aine and hinne > parim_hinne:
            parim_hinne = hinne
            parim_nimi = nimi
    return parim_nimi


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

print(parim_aines(hinded, "Matemaatika"))  # expected output: Mari
