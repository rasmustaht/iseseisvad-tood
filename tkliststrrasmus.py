
# ===== Aritmeetika =====


# A1. Ristküliku pindala ja ümbermõõt
# Tagasta list [pindala, ümbermõõt].
def ristkylik(a, b):
    pindala = a*b
    ümbermõõt = 2*(a+b)
    # Kirjuta siia implementatsioon
    return[pindala, ümbermõõt]


print(ristkylik(3, 4))  # expected output: [12, 14]


# A2. Keskmine
# Tagasta kolme arvu aritmeetiline keskmine.
def keskmine(a, b, c):
    arvud = (a+b+c)/3
    # Kirjuta siia implementatsioon
    return arvud


print(keskmine(2, 4, 9))  # expected output: 5.0


# A3. Jagamine
# Tagasta list [täisarvuline jagatis, jääk, tavaline jagatis].
# Vihje: // , % , /
def jaga(a, b):
    täisjagatis = a//b
    jääk = a%b
    tavajagatis = a/b
    # Kirjuta siia implementatsioon
    return[täisjagatis, jääk, tavajagatis]


print(jaga(17, 5))  # expected output: [3, 2, 3.4]


# A4. Celsius -> Fahrenheit
# Valem: F = C * 9 / 5 + 32. Ümarda tulemus ühe komakohani.
def celsius_fahrenheit(c):
    f = c * 9 / 5 + 32
    # Kirjuta siia implementatsioon
    return round(f, 1)


print(celsius_fahrenheit(21.5))  # expected output: 70.7
print(celsius_fahrenheit(-40))  # expected output: -40.0


# A5. Sekundid -> tunnid, minutid, sekundid
# Tagasta sõne kujul "h:mm:ss", st minutid ja sekundid alati kahekohalised.
# Vihje: // , % ja f-string vormindus {m:02d}
def aeg(sekundid):
    tunnid = sekundid//3600
    minutid = (sekundid%3600)//60
    sekund = sekundid%60
    # Kirjuta siia implementatsioon
    return f"{tunnid}:{minutid:02d}:{sekund:02d}"


print(aeg(3725))  # expected output: 1:02:05
print(aeg(59))  # expected output: 0:00:59


# A6. Tüübiteisendus
# Parameetrid on sõned (nagu input() tagastab). Liida arvud kokku ja tagasta täisarv.
def liida_soned(a, b):
    arvud = int(a) + int(b)
    # Kirjuta siia implementatsioon
    return arvud


print(liida_soned("12", "30"))  # expected output: 42