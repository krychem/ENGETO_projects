# %%
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Kryštof Škach
email: krystof.skach@uochb.cas.cz
"""

#ZADÁNÍ:

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

tabulka = """
+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+
"""

# %%
#úvodní porcování tabulky obsahující přihlašovací data uživatelů a ASCII balast

#odstranění prázdného "enteru" na konci a na začátku a rozdělení na jednotlivé řádky
radky = tabulka.strip("\n").split("\n")

#odstranění řádků neobsahujících žádná data a odstranění mezer tak, aby zůstaly jen hrubé hodnoty
radky_ocistene = []

for radek in radky:
    if "+" not in radek or "-" not in radek:
        radky_ocistene.append(radek.replace(" ",""))

#vytvoření listu s listy obsahující jednotlivé dvojice
list_v_listu = []

for hruba_dvojice in radky_ocistene:
    list_v_listu.append(hruba_dvojice.strip("|").split("|"))

#vytvoření kýženého slovníku bez hlavičky
users = dict()

for jednotliva_data in list_v_listu:
    users.update(list_v_listu[1:])

#snad jsem dosáhl souladu

# %%
login = input("username:")

#kontrola loginu a hesla, pokud dojde ke neúspěšnému pokusu, aplikace se vypne
if login in users:
    heslo = input("password:")
    if heslo == users[login]:
        print(41 * "-")
        print(f"Welcome to the app, {login}")
    else:
        print("password incorrect")
        exit()
else:
    print("unregistered user, terminating program")
    exit()

# %%
print("We have 3 texts to be analyzed.")
print(41 * "-")

volba_textu = input(f"Enter a number btw. 1 and 3 to select:")
print(41 * "-")

text = []

if volba_textu == "1":
    text.append(TEXTS[0].replace("\n    "," "))
elif volba_textu == "2":
    text.append(TEXTS[1].replace("\n    "," "))
elif volba_textu == "3":
    text.append(TEXTS[2].replace("\n    "," "))
else:
    print(f"'{volba_textu}' is not possible")
    exit()

# %%
#převod textu na string:
text_str = str(text)

#ein klassiker spočítání prvků ve stringu, uvažuji-li, že jsou prvky rozděleny mezerou
pocet_slov = len(text_str.split(" "))
print(f"There are {pocet_slov} words to be analyzed.")

#součet slov začínající na velké písmeno
titlecase = 0 #definice proměnné titlecase

for slovo in text_str.split(" "): #definuji slovo podle toho, že je od jiného slova odděleno mezerou
    slovo_ocisteno = slovo.strip(",.") #narazil jsem na to, že následující funkce považuje výsledek za nepravdivý, začíná-li slovo velkým písmenem, ale obsahuje-li zároveň interpunkci
    if slovo_ocisteno.istitle() == True: #definuji, že slovo bez interpunkce začínající na velké písmeno je True
        titlecase += 1
    else:
        titlecase += 0

print(f"There are {titlecase} titlecase words.")

#součet slov psaných kapitálkami
uppercase = 0

#tohle je vlastně analogie k předešlému
for slovo in text_str.split(" "):
    slovo_ocisteno = slovo.strip(",.")
    if slovo_ocisteno.isupper() == True:
        uppercase += 1
    else:
        uppercase += 0

print(f"There are {uppercase} uppercase words.")

#součet slov psaných pouze malými písmeny
lowercase = 0

#tohle je analogie k předešlé analogii
for slovo in text_str.split(" "):
    slovo_ocisteno = slovo.strip(",.")
    if slovo_ocisteno.islower() == True:
        lowercase += 1
    else:
        lowercase += 0

print(f"There are {lowercase} lowercase words.")

#hledání číselných stringů
cislo = 0

for slovo in text_str.split(" "): #vrátil jsem se k projektu po čtyřech dnech a zapomněl jsem, co jsem vlastně myslel - každopádně tady definuji slovo jako element text_str oddělený od ostatnách mezerou
    slovo_ocisteno = slovo.strip(",.") #předpokládám, že Python hodnotu nemusí uznat za numerickou, je-li na ní přilepena tečka či čárka. bojím se to zkoušet, abych to celé nerozhasil a raději tedy přidávám očistu
    if slovo_ocisteno.isnumeric():
        cislo += 1
    else:
        cislo += 0

print(f"There are {cislo} numeric strings.")

#sčítaní hodnot číselných stringů

soucet = 0

for slovo in text_str.split(" "): #definuji slovo jako element oddělený mezerou
    slovo_ocisteno = slovo.strip(",.") #od každého slova raději mažu interpunkci
    if slovo_ocisteno.isnumeric() == True:
        soucet += int(slovo_ocisteno) #cyklus jede a pokud narazí na numerickou hodnotu, převede ji na integer a přičtě k proměnné součet

print(f"The sum of all the numbers is {soucet}.")

# %%
print(41* "-", "LEN|  OCCURRENCES       |NR.", 41* "-", sep="\n")

pocty_pismen = []

for slovo in text_str.split(" "): #opět definice slova
    slovo_ocisteno = slovo.strip(",.'[]") #zjistil jsem, že mi kód do prvního slova počítá i [' a proto to definuji k odstranění funkcí strip také
    if slovo_ocisteno.isnumeric() == False: #předpokládám, že čísla nejsou slova
        pocty_pismen.append(len(slovo_ocisteno)) #kód jede textem, počítá písmena slov a jednotlivé hodnoty postupně přidává do listu pocty_pismen

for i in range(1,(max(pocty_pismen) +1 )):
    mezery = 20 - pocty_pismen.count(i) #aby tabulka dole byla krásná, odpočítal jsem si 20 znaků na jeden řádek ohraničený znakem | a dopočítal, kolik bude vždy chybět
    if len(str(i)) == 1:
        print(f"  {i}|{"*" * pocty_pismen.count(i)}{mezery * " "}|{pocty_pismen.count(i)}") #pro slova o délce 1-9 znaků
    else:
        print(f" {i}|{"*" * pocty_pismen.count(i)}{mezery * " "}|{pocty_pismen.count(i)}") #pro slova o délce 10-99 znaků. zde je patrné, že tento skript se nehodí např. pro jazyk sanskrit, který má slova dlouhá i přes sto znaků
input("\nPRESS ENTER TO EXIT THE APP") #tohle jsem sem dal proto, že když appku pustím v Pythonu, tak se mi všechno od výběru textu dál spustí asi v milisekundě a appka se ihned zavře. tímto jsem to chtěl pojistit, aby si to bob, ann, mike a liz mohli v klidu prohlédnout. to samé bych pravděpodobně asi mohl dát pod funkce exit() při neúspěšných přihlášeních a po špatném výběru textu

