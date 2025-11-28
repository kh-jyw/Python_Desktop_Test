from animal import Animal

class Main:
    def __init__(self):
        self.running = True
          

    def run(self):
        while self.running:
            species = input("Enter an animal (dog, cat, or anything else). Type Q to quit: ").strip()

            if species == "Q" or species == "q":
                print("Exiting")
                self.running = False
            else:
                animal_obj = Animal(species)
                animal_obj.identifty()
if __name__ == "__main__":
    app = Main()
    app.run()