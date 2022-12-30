from csapatok import Csapatok

cs = Csapatok('stadionok.txt')

varos = "Buffalo"
print(f"\n1. feladat: *** {varos}-i csapatok ***\n")

db = cs.csapatok_szama_a_megadott_varosban(varos)
# for csapat in lista:
#     print(f"{csapat.stadion} - {csapat.csapatok_szama}")

if db:
    print(f"Összesen {db} csapat")
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

db = cs.elso_merkozesek_szama_a_megadott_datum_elott(datum)
if db:
    print(f"Összesen {db} csapat")
else:
    print("Nincs a feltételnek megfelelő csapat")


datum = "2000-01-01"
print(f"\n4. feladat: *** Utolsó mérkőzések {datum} után ***\n")

db = cs.utolso_merkozesek_szama_a_megadott_datum_utan(datum)
if db:
    print(f"Összesen {db} csapat")
else:
    print("Nincs a feltételnek megfelelő csapat")
