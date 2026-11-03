import csv
KEHTIVAD_MAARAD = (0, 9, 13, 22, 24)
def loe_tooted(failinimi):
    tooted = []
    with open(failinimi, encoding="utf-8", newline="") as f:
        for rida in csv.DictReader(f, delimiter=";"):
            tooted.append({
                "inventari_nr": rida["inventari_nr"],
                "nimetus": rida["nimetus"],
                "hind_km_ta": float(rida["hind_km_ta"]),
                "laoseis": int(rida["laoseis"]),
                "km_maar": int(rida["km_maar"]),
            })
    return tooted

from decimal import Decimal, ROUND_HALF_UP

def hind_km_ga(hind, maar):
    if hind < 0:
        raise ValueError("Hind ei tohi olla negatiivne")
    d = Decimal(str(hind)) * (Decimal(100) + Decimal(maar)) / Decimal(100)
    return float(d.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def maarade_jaotus(tooted):
    jaotus = {}
    for t in tooted:
        maar = t["km_maar"]
        jaotus[maar] = jaotus.get(maar, 0) + 1
    return jaotus

def laost_otsas(tooted):
    otsas = []
    for t in tooted:
        if t["laoseis"] == 0:
            otsas.append(t)
    return otsas

def kallim_ja_odavam(tooted):
    kallim = max(tooted, key=lambda t: t["hind_km_ta"])
    odavam = min(tooted, key=lambda t: t["hind_km_ta"])
    return kallim, odavam

def lao_vaartus(tooted, km_ga=False):
    summa = 0.0
    for t in tooted:
        if km_ga:
            hind = hind_km_ga(t["hind_km_ta"], t["km_maar"])
        else:
            hind = round(t["hind_km_ta"], 2)
        summa += hind * t["laoseis"]
    return round(summa, 2)

def uus_maar(maar):
    if maar not in KEHTIVAD_MAARAD:
        raise ValueError(f"Kehtetu käibemaksumäär: {maar}")
    return 24 if maar == 22 else maar


def lao_vaartus_uue_maaraga(tooted):
    summa = 0.0
    for t in tooted:
        hind = hind_km_ga(t["hind_km_ta"], uus_maar(t["km_maar"]))
        summa += hind * t["laoseis"]
    return round(summa, 2)

def salvesta_uus_hinnakiri(tooted, failinimi):
    with open(failinimi, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["inventari_nr", "nimetus", "hind_km_ta", "laoseis", "km_maar", "hind_km_ga"])
        for t in tooted:
            maar = uus_maar(t["km_maar"])
            w.writerow([
                t["inventari_nr"],
                t["nimetus"],
                t["hind_km_ta"],
                t["laoseis"],
                maar,
                hind_km_ga(t["hind_km_ta"], maar),
            ])

def main():
    tooted = loe_tooted("tooted.csv")
    print(f"Tooteid kokku: {len(tooted)}")

    print("Tooteid määra kaupa:")
    for maar, arv in sorted(maarade_jaotus(tooted).items()):
        print(f"  {maar}%: {arv}")
        
    otsas = laost_otsas(tooted)
    print(f"Laost otsas: {len(otsas)}")
    for t in otsas:
        print(f"  {t['nimetus']}")
        
    kallim, odavam = kallim_ja_odavam(tooted)
    for silt, t in (("Kõige kallim", kallim), ("Kõige odavam", odavam)):
        print(f"{silt}: {t['nimetus']} ({t['inventari_nr']}), "
              f"{t['hind_km_ta']:.2f} € km-ta, "
              f"{hind_km_ga(t['hind_km_ta'], t['km_maar']):.2f} € km-ga")
        
    km_ta = lao_vaartus(tooted)
    print(f"Lao väärtus km-ta: {km_ta:,.2f} €")
    
    vana = lao_vaartus(tooted, km_ga=True)
    uus = lao_vaartus_uue_maaraga(tooted)
    print(f"Lao väärtus km-ga (vana määr): {vana:,.2f} €")
    print(f"Lao väärtus km-ga (uus määr): {uus:,.2f} €")
    print(f"Vahe: {uus - vana:,.2f} €")
    
    salvesta_uus_hinnakiri(tooted, "tooted_2025_07.csv")

if __name__ == "__main__":
    main()