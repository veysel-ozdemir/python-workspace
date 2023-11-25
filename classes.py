class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along...")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle("Tesla", "Model 3")
# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle("Cadillac", "Escalade")
your_car.get_make_model()
your_car.moves()


# ------------- inheritance -------------
class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print("Flies along...")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model} with a FAA-ID of {self.faa_id}.")


class Truck(Vehicle):
    def moves(self):
        print("Rumbles along...")


class GolfCart(Vehicle):
    pass


cesna = Airplane("Cesna", "Skyhawk", 32212)
mack = Truck("Mack", "Pinnacle")
golfwagon = GolfCart("Yamaha", "GC100")

cesna.get_make_model()
cesna.moves()

mack.get_make_model()
mack.moves()

golfwagon.get_make_model()
golfwagon.moves()

# ------------- polymorphism -------------
# the ability to behave differently in response to the same input messages

for v in (my_car, your_car, cesna, mack, golfwagon):
    v.get_make_model()
    v.moves()
