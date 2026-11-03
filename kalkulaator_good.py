def summa(a, b):
    return a+b

def lahutamine(a, b):
    return a-b

def korrutamine(a, b):
    return a*b

def jagamine(a, b):
    return a/b

def taisarvuline_jagamine(a, b):
    return a//b

x = int(input("sisesta esimene arv: "))
y = int(input("sisesta teine arv: "))
tehe = input("sisesta tehtetüüp: ")

operaatorid = {
    "+":summa(x, y),
    "-":lahutamine(x, y),
    "*":korrutamine(x, y),
    "/":jagamine(x, y),
    "//":taisarvuline_jagamine(x,y)}

print(operaatorid["+"])