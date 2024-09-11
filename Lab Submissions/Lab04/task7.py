
"""
Create a Child class Bus and a parent class Vehicle then make attrivutes accordingly 
"""

class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def calculate_fare(self):
        """Calculate the default fare based on seating capacity."""
        return self.seating_capacity * 100

class Bus(Vehicle):
    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)
   
    def calculate_fare(self):
        """Calculate the fare for a bus with an additional 10% maintenance charge."""
        base_fare = super().calculate_fare()
        maintenance_charge = 0.10 * base_fare
        total_fare = base_fare + maintenance_charge
        return total_fare


vehicle = Vehicle(seating_capacity=40)
print(f"Default fare for Vehicle: Rs.{vehicle.calculate_fare()}")
bus = Bus(seating_capacity=40)
print(f"Total fare for Bus: Rs.{bus.calculate_fare()}")

