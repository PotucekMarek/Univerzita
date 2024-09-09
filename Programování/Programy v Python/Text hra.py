situations = [
    ['Stojíš před dveřmi starého domu. Vidíš klíč visící na háčku vedle dveří. Co uděláš?', 
        [['Otevři dveře.', 1], ['Zaklepej na dveře.', 2], ['Odejdeš pryč.', 3], ['Vezmi klíč.', 14]]],
    ['Vstoupil jsi do temné haly. Před tebou jsou schody nahoru a dveře napravo.', 
        [['Vyjdi po schodech.', 4], ['Vejdi do dveří napravo.', 5], ['Vrať se a zkoumej okolí venku.', 15]]],
    ['Ozvalo se: "Dále." Dveře se samy otevřely a ty vidíš tajemnou postavu uvnitř. Co uděláš?', 
        [['Vstoupíš dovnitř.', 6], ['Zavřeš dveře a odejdeš.', 3]]],
    ['Opustil jsi místo. Hra končí.', []],
    ['Vyšel jsi po schodech a před tebou jsou další dveře. Co uděláš?', 
        [['Otevřeš dveře.', 7], ['Vrátíš se dolů.', 1]]],
    ['Vešel jsi do malé místnosti, kde hoří krb. Na stole leží kniha. Co uděláš?', 
        [['Prozkoumáš knihu.', 8], ['Vrátíš se do haly.', 1]]],
    ['Vstoupil jsi do místnosti, kde stojí tajemná postava. Postava říká: "Hledáš něco?"', 
        [['Ano, hledám odpovědi.', 9], ['Rychle odejdeš.', 3]]],
    ['Za dveřmi je prázdná místnost s oknem. Oknem vidíš temný les.', 
        [['Prozkoumej místnost.', 10], ['Podívej se z okna.', 11], ['Vrať se dolů.', 1]]],
    ['Kniha je plná starých zápisků o magii a historii tohoto domu. Najdeš něco zajímavého?', 
        [['Ano, pokračuj ve čtení.', 12], ['Odložíš knihu a odejdeš.', 1]]],
    ['Postava tě upřeně sleduje. "Odpovědi, které hledáš, tě mohou zničit," varuje.', 
        [['Ignoruj varování a pokračuj.', 12], ['Utečeš z místnosti.', 3]]],
    ['V místnosti není nic zvláštního. Je tu jen starý nábytek a pavučiny.', 
        [['Vrátíš se ke dveřím.', 7]]],
    ['Podíval jsi se z okna a vidíš zvláštní stín pohybující se mezi stromy. Co uděláš?', 
        [['Otevřeš okno a skočíš ven.', 16], ['Ignoruji stín a vrátíš se.', 7]]],
    ['Objevil jsi tajný vchod za knihou. Vedeš dál do temného tunelu. Vstoupíš?', 
        [['Ano, vstoupím do tunelu.', 13], ['Vrátíš se do haly.', 1]]],
    ['Tunel tě zavedl k tajnému východu z domu. Jsi volný! Hra končí.', []],
    ['Sebral jsi klíč. Klíč by mohl být užitečný později.', []],
    ['Vracíš se ke vchodu a prozkoumáváš okolí. Najdeš starý studený šacht, který jde dolů.', 
        [['Sestup do šachty.', 17], ['Vrať se do domu.', 1]]],
    ['Skáčeš ven z okna do lesa a utíkáš pryč od domu.', []],
    ['Sestoupil jsi do šachty a našel jsi podzemní chodbu vedoucí do neznáma.', 
        [['Prozkoumej chodbu.', 18], ['Vrať se nahoru do domu.', 1]]],
    ['Chodba tě dovedla k zapomenutému pokladu. Hra končí.', []]
]

inventory = []

state = [0]

def get_current_situation():
    current_situation_id = state[0]
    return situations[current_situation_id]

def set_current_situation(situation_id):
    state[0] = situation_id

def print_choices(choices):
    for i in range(len(choices)):
        choice = choices[i]
        print(f'{i}. {choice[0]}')

def print_current_situation():
    current_situation_id = state[0]
    situation = situations[current_situation_id]
    print(situation[0])
    if situation[1]:
        print_choices(situation[1])
    else:
        print("Nemáš na výběr, hra končí.")

def add_to_inventory(item):
    inventory.append(item)
    print(f'Přidal jsi {item} do inventáře.')

def use_inventory_item(item):
    if item in inventory:
        inventory.remove(item)
        print(f'Použil jsi {item}.')
        return True
    else:
        print(f'Nemáš {item} v inventáři.')
        return False

def choose(choice_id):
    current_situation = get_current_situation()
    choices = current_situation[1]
    if choices:
        choice = choices[choice_id]
        next_situation_id = choice[1]
        if choice_id == 3 and current_situation[0].startswith('Stojíš před dveřmi'):
            add_to_inventory('klíč')
        set_current_situation(next_situation_id)
    else:
        print("Nemáš na výběr, hra končí.")
        return False
    return True

def play():
    while True:
        print_current_situation()
        current_situation = get_current_situation()
        if not current_situation[1]:
            break  # Konec hry
        choice_id_str = input('Tvá volba: ')
        choice_id = int(choice_id_str)
        if not choose(choice_id):
            break  # Konec hry

play()