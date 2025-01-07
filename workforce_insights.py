# Ülesanne: Tööjõu analüüs sektorite kaupa
fail = "toojoud.txt"
faili_avamine = open(fail,"r",encoding="UTF-8")
linnad = list()
sektorid = list()
naiste_arvud = list()
meeste_arvud = list()
kõrgharidusega_töötajate_arvud = list()

for andmed in faili_avamine:
     linn,sektor,naiste_arv,meeste_arv,kõrgharidusega_töötajad = andmed.split()
     linnad.append(linn)
     sektorid.append(sektor)
     naiste_arvud.append(int(naiste_arv))
     meeste_arvud.append(int(meeste_arv))
     kõrgharidusega_töötajate_arvud.append(int(kõrgharidusega_töötajad))
faili_avamine.close()

#Leia linn, kus kõrgharidusega töötajate osakaal on suurim:
#Arvuta kõrgharidusega töötajate osakaal kõigi töötajate koguarvust (naised + mehed).
#Väljasta selle linna nimi, sektor ja osakaal.
arv = 0
osakaalud = list()
for i in range(len(kõrgharidusega_töötajate_arvud)):
    inimesi_linnas_koos = naiste_arvud[i] + meeste_arvud[i]
    # Panen osakaalu nagu x, siis panen inimesi linna koos nagu 100%
    osakaal = (kõrgharidusega_töötajate_arvud[i] * 100) /inimesi_linnas_koos
    osakaalud.append(round(float(osakaal),2))
print(osakaalud)
for i in range(len(osakaalud)):
    if osakaalud[i]>arv:
        arv = osakaalud[i]
        indeks = i
print("Kõige suurem osakaal on linnas",linnad[indeks], "sektoriga", sektorid[indeks], "osakaaluga(protsendiga)",arv)
# Loenda, mitmes linnas on naiste arv suurem kui meeste arv:
loendur = 0
print("Leiame linnu, kus naiste arv on suurem, kui meeste arv:")
for i in range(len(linnad)):
    if naiste_arvud[i] > meeste_arvud[i]:
        print(linnad[i])
        #Loendan kas sellised linnad eksisteerivad
        loendur = loendur + 1  
if loendur == 0:
    print("Kahjuks, selliseid linnu pole, kus naiste arv on suurem kui meeste arv")

# Küsi kasutajalt kõrgharidusega inimeste arvuline piirmäär.
# Kuvage tabelina kõik linnad ja sektorid, kus kõrgharidusega inimeste arv on sellest suurem.
# Kui selliseid andmeid ei ole, trüki sobiv teade.
kasutaja_piirmäär = int(input("Sisesta arvulise piirmääru:"))
print("Tabel, kus kõrgharidusega inimeste arv on sisestatud piirmäärusest suurem.")
print(f"{'Linn':<10}{'Sektor':<10}{'Arv':<10}")
loendur2 = 0
for i in range(len(linnad)):
    if kõrgharidusega_töötajate_arvud[i] > kasutaja_piirmäär:
        print(f"{linnad[i]:<10}{sektorid[i]:<10}{kõrgharidusega_töötajate_arvud[i]:<10}")
        loendur2 = loendur2 + 1
if loendur2 == 0:
    print("Kahjuks, kõrgharidusega inimeste arv, mis sisestatud piirmäärusest suurem pole!")