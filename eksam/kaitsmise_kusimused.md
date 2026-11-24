# Kaitsmise harjutusküsimused

Eksamil tuleb oma koodi selgitada. Allpool on tõenäolised küsimused ja lühikesed vastused.

## Eksamiülesande kohta

**1. Miks kasutad `with open(...)`?**
`with` sulgeb faili automaatselt, kui plokk lõpeb, ka siis, kui tekib viga.

**2. Miks `encoding="utf-8"`?**
Failis on täpitähed (ü, õ). Ilma selleta võib Windowsis tekkida viga või valed tähed.

**3. Mida teeb `rida.strip().split(",")`?**
`strip()` eemaldab rea algusest ja lõpust tühikud ning reavahetuse (`\n`).
`split(",")` tükeldab rea komade kohalt listiks: `["Mari", " Matemaatika", " 5"]`.

**4. Miks `int(...)`?**
Failist loetud andmed on alati sõned. Hinnetega arvutamiseks on vaja arve.

**5. Mis vahe on listil, tuple'il ja sõnastikul?**
- list `[]` on järjestatud ja muudetav
- tuple `()` on järjestatud, aga muuta ei saa
- sõnastik `{}` koosneb paaridest võti → väärtus; väärtuse saad kätte võtme järgi

**6. Kuidas sõnastikku loendad/summeerid?**
Kontrollid `if nimi in summad:`. Kui võti on olemas, liidad juurde. Kui ei ole, lood uue võtme.
Sama muster on failis `tk_list_str_dict.py` (`loenda_sonad`).

**7. Mida teeb `sorted(..., key=..., reverse=True)`?**
`key` ütleb, mille järgi sorteerida (siin keskmise hinde ehk paari teise elemendi `paar[1]` järgi).
`reverse=True` sorteerib suuremast väiksemaks.

**8. Mis on `lambda`?**
Lühike nimeta funktsioon. `lambda paar: paar[1]` on sama mis
```python
def votta_keskmine(paar):
    return paar[1]
```

**9. Mida tagastab `.items()`?**
Sõnastiku võti-väärtus paarid tuple'itena: `('Mari', 4.67)`.

**10. Mis vahe on `return` ja `print` vahel?**
`return` annab väärtuse funktsioonist välja, et seda saaks edasi kasutada. `print` ainult näitab väärtust ekraanil.

## Sinu kodused tööd (võidakse küsida)

| Fail | Mida teab olla selgitada |
|---|---|
| `tk_aritmeetika.py` | `//` täisarvuline jagamine, `%` jääk, `/` tavaline jagamine; `f"{m:02d}"` |
| `tk_list_str_dict.py` | for-tsükkel, `append` vs `extend`, `.lower()`, sõnastikku loendamine |
| `ülesanded123456.py` | `isalpha()`, `continue` |
| `vinuulivalija.py` | faili lugemine, `split(",")`, tingimus `soovitud == "" or ...` |
| `poenimekiri.py` | hulgad (`set`), `&` ühisosa, `-` vahe, `|` ühend; `yield` |
| `list_find_largest_number_muudetud.py` | teise suurima leidmine, `float('-inf')` |
| `genepykuidasmaksta.py` | `//` ja `%` rahatähtede arvutamisel |

## ⚠️ Enne eksamit paranda

- **`genepykuidasmaksta.py`**: `result[value] = 1` peaks olema `result[value] = count`.
  Praegu näitab kood alati ühte kupüüri, isegi kui neid on vaja mitu.
- **`kalkulaator_bad.py`** ei käivitu üldse (süntaksivead). Kui seda faili näitad, ütle, et see on teadlikult "halb" versioon.
- **`kalkulaator_good.py`**: sõnastikus arvutatakse kõik tehted kohe ära (ka jagamine nulliga annaks vea),
  ja lõpus prinditakse alati `"+"`. Peaks olema `print(operaatorid[tehe])`.
- **`poenimekiri.py`**: ülesanne nõuab, et tähesuurust ei muudetaks, aga kood kasutab `.lower()`.
  `leia_puuduvad` ja `leia_korduvad` on ka veel kirjutamata.
