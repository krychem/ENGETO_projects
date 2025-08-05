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
#v první verzi jsem si tento slovník vytvářel složitě z tabulky ze zadání. měl jsem umanutí, že se to po nás určiě chce, protože mi to přišlo jako zajimavé cvičení se stringy. navíc jsem to považoval za univerzálnější řešení pro případ, že bych teoreticky měl mnohem delší seznam uživatelů - abych to pak nemusel přepisovat ručně
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

oddelovac = 41 * "-" #pro jednoduchost si definuji oddělovač textu z pomlček

login = input("username:")
heslo = input("password:")

#kontrola loginu a hesla, pokud dojde ke neúspěšnému pokusu, aplikace se vypne
if login in users and users[login] == heslo: #v minulé verzi jsem měl dvě větve - jedna pro login a druhá pro heslo, přičemž program reagoval zvlášť na jeden či druhý chybný údaj. Takto to prostě kontroluje obě zároveň a je to.
    print(oddelovac)
    print(f"Welcome to the app, {login}")
else:
    print("unregistered user, terminating program")
    input("\nPRESS ENTER TO EXIT THE APP") #vkládám, aby i nesprávný uživatel mohl vidět, co se stalo, protože v Pythonu na PC se v podstatě ihned okno zavře a uživatel nic nevidí
    exit()

# %%
print("We have 3 texts to be analyzed.")
print(oddelovac)

volba_textu = input(f"Enter a number btw. 1 and 3 to select:")
print(oddelovac)

if volba_textu.isdigit() and 1 <= int(volba_textu) <= len(TEXTS): #pojistka, kdyby uživatel zadal nečíselný input, nebo vyšší hodnotu
    text = TEXTS[int(volba_textu) - 1] #text tedy odpovídá stringu uživatelovi volby o příslušném pořadí v proměnné TEXTS
else:
    print("Invalid input. Terminating program.")
    input("\nPRESS ENTER TO EXIT THE APP") #opět vkládám, aby bylo vidět, co se děje
    exit()

#odstranění bílých znaků
bile_znaky = ["\n", "\t"] #definice bilých znaků

for znak in bile_znaky: #for smycka jede a nalezne-li bílý znak, nahradí jej mezerou
    if znak in text:
        text = text.replace(znak, " ")

text_cisty = "" #definice čistého stringu text, zatím prázdná
mezera_predtim = False #říká, že předešlá hodnota nebyla mezera

#odstranění mezer o počtu vyšším, než jedna
for znak in text: #jede znak po znaku...
    if znak == " ": #...pokud narazí na mezeru...
        if not mezera_predtim: #...pokud předchozí znak nebyla mezera, ale nyní je -> True a vstupuje do smyčky
            text_cisty += " " #...přidá mezeru do očištěného textu...
            mezera_predtim = True #...přepne z False na True -> pokračuje nahoru k vnějšímu if a pokud je to opět mezera, vychází False a podmínka se nespustí a cyklus se opakuje, dokud nenarazí na jiný znak.
    else:
        text_cisty += znak #nebyla to mezera, znak se normálně přidává
        mezera_predtim = False #právě zpracovaná hodnota nebyla mezera

text = text_cisty #uložení pročištěného kódu zpět do proměnné "text", abych nemusel přepisovat celý kód, který jsem v napsal pro minulou verzi

# %%
mnozina_slov = text.split(" ") #rozdělení textu na seznam slov podle mezer
print(f"There are {len(mnozina_slov)} words to be analyzed.") #výpočet počtu slov jako součet prvků stringu

hodnoty = { #v předešlé verzi jsem měl jen výčet proměnných, takto ve slovníku se to jeví jako elegantnější řešení, neboť jsou všechny hodnoty pohromadě
    "cislo": 0,
    "soucet": 0,
    "titlecase": 0,
    "uppercase": 0,
    "lowercase": 0
}

interpunkce_etc = ".,()[]\"'" #proměnná obsahující interpunke a další znaky pro následná čištění textu, v minulé verzi jsem měl ve strip funkci jen ",.", nyní dělám obecnější

#součty výskytů různých typů slov a čísel
for slovo in mnozina_slov: #definuji slovo podle toho, že je od jiného slova odděleno mezerou
    slovo_ocisteno = slovo.strip(interpunkce_etc) #odstranění nechtěných znaků
    slovo_bez_carky = slovo_ocisteno.replace(",", "") #pokud má číslo čárku a za předpokladu, že se v textu nevyskytují floaty -> tisíc je tedy zapsán 1,000 -> převod na 1000
    if slovo_bez_carky.isnumeric(): # nejdřív testuji čísla
        hodnoty["cislo"] += 1 #zaznamená se do počtu čísel...
        hodnoty["soucet"] += int(slovo_bez_carky) #...a přičte se jeho hodnota, kdy je nutné převést string na integer
    elif slovo_ocisteno.istitle(): #definuji, že slovo bez interpunkce začínající na velké písmeno je True, tato logika pracuje i v následujících větvích
        hodnoty["titlecase"] += 1
    elif slovo_ocisteno.isupper():
        hodnoty["uppercase"] += 1
    elif slovo_ocisteno.islower():
        hodnoty["lowercase"] += 1

print(f"There are {hodnoty['titlecase']} titlecase words.") #teraz tlač 
print(f"There are {hodnoty['uppercase']} uppercase words.")
print(f"There are {hodnoty['lowercase']} lowercase words.")
print(f"There are {hodnoty['cislo']} numeric strings.")
print(f"The sum of all the numbers is {hodnoty['soucet']}.")

# %%
print(oddelovac, "LEN|  OCCURRENCES       |NR.", oddelovac, sep="\n") #hlavička

pocty_pismen = []

for slovo in mnozina_slov: #definice slova
    slovo_ocisteno = slovo.strip(interpunkce_etc) #odstranění případných speciálních znaků
    cislo_s_interpunkci = slovo_ocisteno.replace(",", "").replace(".", "") #oproti minulé verzi jsem si uvědomil, že by kód asi považoval za nečíselné stringy i čísla s desetinnou tečkou a čárkou - toto je jejich zohlednění
    if not cislo_s_interpunkci.isnumeric():
        pocty_pismen.append(len(slovo_ocisteno))

hvezda = "*" #měl jsem v komentáři k první verzi připomínku k nejasnému syntaxu, abych zamezil kumulaci uvozovek v kódu finálního grafu, dávám si hvězdu jako proměnnou
sirka_grafu = 20 #šířku grafu volím 20 znaků proto, že mi to přijde jako dostatečná hodnota pro přiměřeně dlouhé texty

for i in range(1, max(pocty_pismen) + 1): #i coby klouzavá hodnota představující v cyklu různé délky slov
    mezery = sirka_grafu - pocty_pismen.count(i) #výpočet počtu mezer tak, aby to bylo vždy 20 znaků - rozdíl šířky grafu a počtu slov o četnosti i
    if len(str(i)) == 1: #řádek pro jednociferné
        print(f"  {i}|{hvezda * pocty_pismen.count(i)}{' ' * mezery}|{pocty_pismen.count(i)}") #řádek pro jednociferné
    else:
        print(f" {i}|{hvezda * pocty_pismen.count(i)}{' ' * mezery}|{pocty_pismen.count(i)}") #řádek pro dvouciferné - nepředpokládám slova o počtu písmen na tři cifry

input("\nPRESS ENTER TO EXIT THE APP") #vkládám input pro únik z programu, protože při otevření v pythonu na PC se program zavře v podstatě okamžitě po zadání čísla studovaného textu