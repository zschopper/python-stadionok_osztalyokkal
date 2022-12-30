from csapatok import Csapatok

cs = Csapatok('stadionok.txt')

# 1. feladat
varos = "New York"
print(f"\n1. feladat: *** {varos}-i stadionok ***\n")

db = cs.stadionok_szama_a_megadott_varosban(varos)

if db:
    print(f"Összesen {db} csapat")
else:
    print("Nincs a feltételnek megfelelő csapat")

# 2. feladat

print("\n2. feladat: *** Csapatok ***")

db = cs.csapatok_szama()

if db:
    print(f"A csapatok darabszáma: {db}")
else:
    print("Nincs csapat a listán")

# 3. feladat

datum = "1900-01-01"
print(f"\n3. feladat: *** Kezdő mérkőzések {datum} előtt ***\n")

db = cs.elso_merkozesek_szama_a_megadott_datum_elott(datum)
if db:
    print(f"Összesen {db} csapat")
else:
    print("Nincs a feltételnek megfelelő csapat")

# 4. feladat

datum = "2000-01-01"
print(f"\n4. feladat: *** Utolsó mérkőzések {datum} előtt ***\n")

db = cs.utolso_merkozesek_szama_a_megadott_datum_elott(datum)
if db:
    print(f"Összesen {db} csapat")
else:
    print("Nincs a feltételnek megfelelő csapat")

# 5. feladat

varos = "Buffalo"
print(f"\n5. feladat: *** {varos}-i csapatok ***\n")

db = cs.csapatok_szama_a_megadott_varosban(varos)

if db:
    print(f"Összesen {db} csapat")
else:
    print("Nincs a feltételnek megfelelő csapat")

