class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def addPassenger(self, name):
        if not self.openSeats():
            return False
        self.passengers.append(name)
        return True

    def openSeats(self):
        return self.capacity - len(self.passengers)
    

    def removePassenger(self, name):
        if self.passengers:
            self.passengers.remove(name)
            return True
        else:
            return False

flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]

for person in people:
    if flight.addPassenger(person):
        print(f"Added {person} successfully.")
    else:
        print(f"No available seats for {person}.")

flight.removePassenger("Harry")
flight.addPassenger("Ginny")
print(flight.passengers)