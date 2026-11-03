def summa(a, b):
    return a+b

def lahutamine(a, b):
    return a-b

def korrutamine(a, b):
    return a*b

def jagamine(a, b):
    return a/b


x = int(input("sisesta esimene arv: "))
y = int(input("sisesta teine arv: "))
tehe = input("sisesta tehtetüüp")

print(x, tehe, y)

operaatorid = {
    "+":summa(x, y)}, lahutamine, korrutamine, jagamine
for operaator in operaatorid 

if tehe == "+":
    print(x+y)
if tehe == "-":
    print(x-y)
if tehe == "*":
    print(x*y)
if tehe == "/":
    print(x/y)
else:
    print("ei oska arvutada")