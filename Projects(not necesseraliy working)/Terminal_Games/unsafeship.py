import random


antalrader = 10
antalkolumner = 10

bräda = []
rad = []
tom_bräda = []
antalbåt = 1
for r in range(antalkolumner):
    rad.append("~")

print("\n")

for k in range(antalrader):
    bräda.append(list(rad))
for k in range(antalrader):
    tom_bräda.append(list(rad))

rad0 = []

for k in range(ord('A'), ord('A')+antalkolumner):
    rad0.append(chr(k))
rad0.insert(0, "  ")


def skapa_plan(var=rad0):
    for b in rad0:
        print(b, end=" ")
    print()

    for r in range(antalrader):

        print(str(r+1) + " ", end="")
        if r != 9:
            print(" ", end="")
        for k in bräda[r]:
            print(k, end=" ")
        print()


ockuperat = []
båtkoordinater = []


def horizontell_båtläggare(längd, ockuperat=ockuperat):

    check = True

    while check == True:
        x = random.randint(0, 10-längd)
        y = random.randint(0, 9)

        for k in range(längd):
            if (x+k, y) not in ockuperat:
                check = False
            elif (x+k, y) in ockuperat:
                check = True
                break

    for i in range(längd):
        bräda[y][x + i] = ":"
        båtkoordinater.append((x + i, y))

        lista = [(x + i, y), (x + i, y - 1), (x + i, y + 1), (x + längd, y), (x - 1, y)]
        ockuperat.extend(lista)


def vertikal_båtläggare(längd, ockuperat=ockuperat):

    check = True

    while check == True:
        x = random.randint(0, 9)
        y = random.randint(0, 10-längd)

        for k in range(längd):
            if (x, y+k) not in ockuperat:
                check = False
            elif (x, y+k) in ockuperat:
                check = True
                break

    for i in range(längd):
        bräda[y + i][x] = ":"
        båtkoordinater.append((x, y + i))

        lista = [(x, y + i), (x - 1, y + i), (x + 1, y + i), (x, y + längd), (x, y - 1)]
        #buffer for future list of only colons
        ockuperat.extend(lista)


båtar = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]


def skapa_bräde(spelplan):
    for p in range(10):
        båtindex = p
        höger_eller_ner = random.randint(0, 1)
        if höger_eller_ner == 0:
            horizontell_båtläggare(längd=båtar[p])
        else:
            vertikal_båtläggare(längd=båtar[p])


def skapa_tom_plan(var=rad0):
    for b in rad0:
        print(b, end=" ")
    print()

    for r in range(antalrader):

        print(str(r+1) + " ", end="")
        if r != 9:
            print(" ", end="")
        for k in tom_bräda[r]:
            print(k, end=" ")
        print()


skapa_bräde(spelplan=tom_bräda)
skapa_tom_plan()
counter = 20
träffade = []

while counter != 0:

    skott = list(input("Vilka koordinater vill du skjuta på?\n").upper())
    if skott[-1] == "0":
        skott[1] = "10"
        skott.pop()

    skott = (ord(skott[0]) - 65, int(skott[1]) - 1)

    for i in range(len(båtkoordinater)):
        if skott in båtkoordinater:
            tom_bräda[skott[1]][skott[0]] = "x"
            if skott in träffade:
                print("Redan träffad, skjut igen")
            else:
                print("Träff")
                counter = counter - 1
                print(counter, "kvar")
            träffade.append(skott)
            break
        elif skott not in båtkoordinater:
            print("plums")
            tom_bräda[skott[1]][skott[0]] = "0"
    skapa_tom_plan()


if counter == 0:
    print("Du vinner")
