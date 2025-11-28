class Animal:
    def __init__(self, species):
        self.species = species.lower()

    def identifty(self):
        if self.species =="dog":
            print("woof woof!")
        elif self.species =="cat":
            print("meow meow!")
        else:
            print(f"ALIEN FOUND! ({self.species})")