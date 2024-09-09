# Jednoduchá textová hra.
#
# Hráč je v určité situaci a může si z voleb, které situace nabízí, vybrat.
# Vybráním volby se hráč dostane do další situace.
# Hra končí ve chvíli, kdy se hráč dostane do situace, která nenabízí žádnou volbu.

class Choice:
    """Volba hráče určuje popis a situaci, do které se hráč dostane po jejím vybrání."""
    def __init__(self):
        self.description = "Missing description."
        self.target_situation = EMPTY_SITUATION

    def get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description
        return self

    def get_target_situation(self):
        return self.target_situation

    def set_target_situation(self, target_situation):
        if not isinstance(target_situation, Situation):
            raise TypeError("Taget situation must be an instance of class Situation.")
        self.target_situation = target_situation
        return self

    def print(self, index):
        print(str(index + 1) + ". " + self.get_description())
        return self
        
class Situation:
    """Hráčova situace je dána popisem a možnostmi, které nabízí."""
    def __init__(self):
        self.description = "Missing description."
        self.choices = []

    def get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description
        return self

    def get_choices(self):
        return self.choices[:]

    def check_choices(self, choices):
        for choice in choices:
            if not isinstance(choice, Choice):
                raise TypeError("Choices of situation must be instances of class Choice.")
        return self
    
    def set_choices(self, choices):
        self.check_choices(choices)
        self.choices = choices[:]
        return self
        
    def get_choice(self, index):
        return self.get_choices()[index]

    def add_choice(self, choice):
        self.set_choices(self.get_choices() + [choice])
        return self

    def print_description(self):
        print(self.description)
        return self

    def is_end(self):
        return self.get_choices() == [] # Situace je konečná, pokud nenabízí žádné volby.

    def print_choices(self):
        choices = self.get_choices()
        for i in range(len(choices)):
            choice = choices[i]
            choice.print(i)
        return self

    def print(self):
        self.print_description()
        self.print_choices()
        return self

    def get_user_choice_index(self):
        """Získá volbu od uživatele."""
        choices_count = len(self.get_choices())
        while True:
            choice_str = input("Tvá volba: ")
            try:
                choice_index = int(choice_str) - 1
                if not 0 <= choice_index < choices_count:
                    raise Exception
                print()
                return choice_index               
            except:
                print("Špatně zadaná volba. Zkuste znovu.")
            

        
    def user_choice(self):
        """Nechá hráče vybrat volbu ze zadaných voleb."""
        self.print()
        choice_index = self.get_user_choice_index()
        choice = self.get_choice(choice_index)
        return choice.get_target_situation()

EMPTY_SITUATION = Situation()

class Game:
    """Hra je dána výchozí a aktuální situací."""
    def __init__(self):
        self.initial_situation = EMPTY_SITUATION
        self.current_situation = EMPTY_SITUATION

    def get_current_situation(self):
        return self.current_situation

    def set_current_situation(self, current_situation):
        if not isinstance(current_situation, Situation):
            raise TypeError("Current situation must be an instance of class Situation.")
        self.current_situation = current_situation
        return self

    def get_initial_situation(self):
        return self.initial_situation

    def set_initial_situation(self, initial_situation):
        if not isinstance(initial_situation, Situation):
            raise TypeError("Initial situation must be an instance of class Situation.")
        self.initial_situation = initial_situation
        return self

    def start(self):
        """Vrátí stav hry na začátek."""
        self.set_current_situation(self.get_initial_situation())
        return self

    def is_end(self):
        """Rozhodne, zda je hra v koncové situaci."""
        return self.get_current_situation().is_end()
    
    
    def play(self):
        """Spustí hru."""
        self.start()
        while not self.is_end():
            situation = self.get_current_situation()
            target_situation = situation.user_choice()
            self.set_current_situation(target_situation)
        self.get_current_situation().print()
        return self
        
    

    
# Vytvoření hry.
s1 = Situation().set_description("Stojíš u dveří.")
s2 = Situation().set_description("Máš před sebou otevřené dveřme.")
s3 = Situation().set_description("Jsi ve tmě. Konec hry.")
s4 = Situation().set_description("Nic se nestalo.")


s1.add_choice(Choice().set_description("Otevři dveře.").set_target_situation(s2))
s1.add_choice(Choice().set_description("Zaklepej.").set_target_situation(s4))

s2.add_choice(Choice().set_description("Vejdi.").set_target_situation(s3))
s4.add_choice(Choice().set_description("Otevři dveře.").set_target_situation(s2))
g = Game().set_initial_situation(s1)

# Start hry.
g.play()
