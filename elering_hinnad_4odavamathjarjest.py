"""Pärib Eleringi kogulehelt (dashboard.elering.ee) tänased päev-ette elektrihinnad,
prindib need ja salvestab faili hinnad.csv.

API dokumentatsioon: https://dashboard.elering.ee/assets/swagger-ui/index.html
Vastus tuleb 15-minutiliste intervallidena: {'timestamp': unix-aeg, 'price': EUR/MWh}.
Ajad arvutatakse Eesti ajavööndis (Europe/Tallinn), sõltumata arvuti enda seadetest.

Käivita:  python elering_hinnad.py
"""
import csv
from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo

import requests

API = "https://dashboard.elering.ee/api/nps/price"
FAILI_NIMI = "hinnad.csv"
EESTI = ZoneInfo("Europe/Tallinn")


def tanased_hinnad() -> dict[datetime, float]:
    """Tagastab tänased hinnad sõnastikuna {Eesti kellaaeg: hind EUR/MWh}.

    API ootab algus- ja lõpuaega koos ajavööndiga (ISO 8601), lõpp on kaasa arvatud,
    seega küsime Eesti aja järgi 00:00:00 kuni 23:59:59.
    """
    tana = datetime.now(EESTI).date()
    algus = datetime.combine(tana, time.min, tzinfo=EESTI)
    lopp = datetime.combine(tana, time.max, tzinfo=EESTI)
    vastus = requests.get(API, params={"start": algus.isoformat(), "end": lopp.isoformat()})
    vastus.raise_for_status()

    hinnad = {}
    for kirje in vastus.json()["data"]["ee"]:
        aeg = datetime.fromtimestamp(kirje["timestamp"], EESTI)
        hinnad[aeg] = kirje["price"]
    return hinnad


def salvesta_csv(hinnad: dict[datetime, float], failinimi: str) -> None:
    """Kirjutab hinnad CSV-faili: esimesel real veerupäised, edasi aeg;hind."""
    with open(failinimi, "w", newline="") as f:
        kirjutaja = csv.writer(f, delimiter=";")
        kirjutaja.writerow(["aeg", "hind_eur_mwh"])
        for aeg, hind in hinnad.items():
            kirjutaja.writerow([f"{aeg:%Y-%m-%d %H:%M}", hind])

def odavaim_aken(hinnad: dict[datetime, float], tunde: int = 4, alates: datetime | None = None):
    """Leiab odavaima järjestikuse tundide lõigu.

    Tagastab (algus, lõpp, keskmine hind EUR/MWh) või None, kui andmeid on liiga vähe.
    Kui 'alates' on antud, arvestatakse ainult sellest hetkest alates algavaid lõike.
    """
    ajad = sorted(hinnad)
    if alates is not None:
        ajad = [a for a in ajad if a >= alates]
    n = tunde * 4  # 15-minutilisi intervalle tunnis on 4
    if len(ajad) < n:
        return None

    parim_summa = None
    parim_algus = 0
    for i in range(len(ajad) - n + 1):
        summa = sum(hinnad[a] for a in ajad[i:i + n])
        if parim_summa is None or summa < parim_summa:
            parim_summa = summa
            parim_algus = i

    algus = ajad[parim_algus]
    lopp = ajad[parim_algus + n - 1] + timedelta(minutes=15)
    return algus, lopp, parim_summa / n

def main() -> None:
    hinnad = tanased_hinnad()
    salvesta_csv(hinnad, FAILI_NIMI)
    print(f"Salvestatud faili {FAILI_NIMI}\n")
    print(f"{datetime.now(EESTI):%Y-%m-%d} elektrihinnad ({len(hinnad)} intervalli):")
    for aeg, hind in hinnad.items():
        print(f"  {aeg:%H:%M}  {hind:7.2f} EUR/MWh")

    odavaim = min(hinnad, key=hinnad.get)
    kalleim = max(hinnad, key=hinnad.get)
    print(f"\nOdavaim: {odavaim:%H:%M} {hinnad[odavaim]:.2f} EUR/MWh")
    print(f"Kalleim: {kalleim:%H:%M} {hinnad[kalleim]:.2f} EUR/MWh")
    
    tulemus = odavaim_aken(hinnad, tunde=4)
    if tulemus:
        algus, lopp, keskmine = tulemus
        kulu = keskmine / 1000 * 1 * 4
        print(f"\nOdavaim 4 tunni järjest: {algus:%H:%M} kuni {lopp:%H:%M}")
        print(f"Keskmine hind: {keskmine:.2f} EUR/MWh ({keskmine / 10:.2f} senti/kWh)")
        print(f"1 kW tarbija 4 tunni kulu: {kulu:.3f} EUR (ilma maksude ja võrgutasudeta)")


if __name__ == "__main__":
    main()