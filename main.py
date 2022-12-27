from csapatok import Csapatok

cs = Csapatok('stadionok.txt')

print("B feladat: *** Csapatok ***")

lista = cs.get_lista()
# for csapat in lista:
#     print(csapat)

if len(lista):
    print(f"A csapatok darabszáma: {len(lista)}")
else:
    print("Nincs csapat a listán")

varos = "New York"
print(f"\nC feladat: *** {varos}-i csapatok ***\n")

lista = cs.varosi_lista(varos)
for csapat in lista:
    print(f"{csapat.stadion} - {csapat.csapatok_szama}")

if len(lista):
    print(f"Összesen {len(lista)} csapat")
else:
    print("Nincs a feltételnek megfelelő csapat")

honapok = ('', 'január', 'február', 'március', 'április', 'május', 'június', 'július', 'augusztus', 'szeptember', 'október', 'november', 'december')
honap = 9
print(f"\nD feladat: *** Kezdő mérkőzések {honapok[honap]} hónapból ***\n")

lista = cs.elso_merkozes_honapja(honap)
# for csapat in lista:
#     print(f"{csapat.stadion} - {csapat.elso_merkozes}")

if len(lista):
    print(f"Összesen {len(lista)} csapat")
else:
    print("Nincs a feltételnek megfelelő csapat")
