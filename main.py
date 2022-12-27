from csapatok import Csapatok

cs = Csapatok('stadionok.txt')

varos = "New York"
print(f"\n1. feladat: *** {varos}-i csapatok ***\n")

lista = cs.varosi_lista(varos)
for csapat in lista:
    print(f"{csapat.stadion} - {csapat.csapatok_szama}")

if len(lista):
    print(f"Összesen {len(lista)} csapat")
else:
    print("Nincs a feltételnek megfelelő csapat")

print("\n2. feladat: *** Csapatok ***")

lista = cs.get_lista()
# for csapat in lista:
#     print(csapat)

if len(lista):
    print(f"A csapatok darabszáma: {len(lista)}")
else:
    print("Nincs csapat a listán")

datum = "1900-01-01"
print(f"\n3. feladat: *** Kezdő mérkőzések {datum} előtt ***\n")

lista = cs.elso_merkozes_datum_elott(datum)
# for csapat in lista:
#     print(f"{csapat.stadion} - {csapat.elso_merkozes}")

if len(lista):
    print(f"Összesen {len(lista)} csapat")
else:
    print("Nincs a feltételnek megfelelő csapat")

datum = "2000-01-01"
print(f"\n4. feladat: *** Utolsó mérkőzések {datum} után ***\n")

lista = cs.utolso_merkozes_datum_utan(datum)
# for csapat in lista:
#     print(f"{csapat.stadion} - {csapat.utolso_merkozes}")

if len(lista):
    print(f"Összesen {len(lista)} csapat")
else:
    print("Nincs a feltételnek megfelelő csapat")
