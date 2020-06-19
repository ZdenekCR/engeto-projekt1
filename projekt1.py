from pprint import pprint as pp
ODDELOVAC = 30 * '='
print(ODDELOVAC)
print("Vitej v nasem programu!")
print(ODDELOVAC)
db_hesel = {
'bob': '123', 
'ann': 'pass123', 
'mike': 'password123', 
'liz': 'pass123',
}
JMENO = input("Zadej svoje jmeno: ")
HESLO = input("Zadej svoje heslo: ")
#if JMENO in db_hesel.keys() and HESLO == db_hesel[JMENO]:
if db_hesel.get(JMENO)==HESLO:
    print("Jsi prihlasen.")
else:
    print("Zadal jsi chybne jmeno nebo heslo.")
    exit()

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''
At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''
The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

for i in TEXTS:
    print(i)
print(ODDELOVAC)
text = int(input("Vyber si jaky odstavec chces zpracovavat?"))
if text > 3:
    print("Mame jenom tri odstavce")
    exit()
ODST = TEXTS[text-1]
rozdeleni = ODST.split()
cisty_list = [i.strip(",.") for i in rozdeleni]
print(ODDELOVAC)
print(f"Pocet slov v odstavci je: {len(cisty_list)}")
count = 0
male = 0
velke = 0
cis = 0
soucet = []
delka_slova = {}
for i in cisty_list:
    if i.istitle():
        count = count + 1
    if i.islower():
        male = male + 1
    if i.isnumeric():
        cis = cis + 1
    if i.isnumeric():
        soucet.append(int(i))
    if i.isupper():
        velke = velke + 1
    else:
        delka_slova[len(i)] = delka_slova.setdefault(len(i), 0) + 1

print(ODDELOVAC)
print(f"Pocet slov majici na zacatku velke pismeno je: {count}.")
print(ODDELOVAC)
print(f"Pocet slov psany malymi pismeny je: {male}.")
print(ODDELOVAC)
print(f"Pocet slov psany velkymi pismeny je: {velke}.")
print(ODDELOVAC)
print(f"Pocet cisel v textu je: {cis}.")
print(ODDELOVAC)
#sort = sorted(delka_slova, key=delka_slova.get, reverse=True)
sort = sorted(delka_slova, reverse=True)
print("Nejcastejsi pocet pismen ve slove.")
for i in sort:
    print(i, delka_slova.get(i) * "*", delka_slova.get(i), "x")
konec = sum(soucet)
print(ODDELOVAC)
print(f"Soucet vsech cisel v textu je {float(konec)}.")
print(ODDELOVAC)
print("Dekujeme za vyuziti programu.")