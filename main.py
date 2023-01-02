from csapatok import Csapatok

cs = Csapatok('stadionok.txt')

# 1. feladat
varos = "New York"
print("\n1. feladat")

db = cs.stadionok_szama_a_megadott_varosban(varos)

if db:
    print(f"Összesen {db} {varos}-i stadion van")
else:
    print(f"Nincs {varos}-i stadion")

# 2. feladat

print("\n2. feladat")

db = cs.csapatok_szama()

if db:
    print(f"A csapatok darabszáma: {db}")
else:
    print("Nincs csapat a listán")

# 3. feladat

datum = "1900-01-01"
print("\n3. feladat")

db = cs.elso_merkozesek_szama_a_megadott_datum_elott(datum)
if db:
    print(f"Összesen {db} stadionban volt mérkőzés {datum} előtt")
else:
    print(f"Egyik stadionban sem volt mérkőzés {datum} előtt")

# 4. feladat

datum = "2000-01-01"
print("\n4. feladat")

db = cs.utolso_merkozesek_szama_a_megadott_datum_elott(datum)
if db:
    print(f"Összesen {db} stadionban nem volt mérkőzés {datum} óta")
else:
    print(f"Nincs olyan stadion, ahol nem volt mérkőzés {datum} óta")

# 5. feladat

varos = "Buffalo"
print("\n5. feladat")

db = cs.csapatok_szama_a_megadott_varosban(varos)

if db:
    print(f"Összesen {db} db {varos}-i csapat van")
else:
    print(f"Nincs {varos}-i csapat")
