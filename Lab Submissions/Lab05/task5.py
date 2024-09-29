from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, rental_price):
        self.make = make
        self.model = model
        self.rental_price = rental_price
        self.is_available = True

    @abstractmethod
    def display_details(self):
        pass

    def check_availability(self):
        return self.is_available

    def rent(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_vehicle(self):
        self.is_available = True

    def calculate_rental_cost(self, rental_period):
        return rental_period * self.rental_price


class Car(Vehicle):
    def __init__(self, make, model, rental_price):
        super().__init__(make, model, rental_price)

    def display_details(self):
        return f"Car: {self.make} {self.model}\nRental Price: ${self.rental_price:.2f}\n"


class SUV(Vehicle):
    def __init__(self, make, model, rental_price):
        super().__init__(make, model, rental_price)

    def display_details(self):
        return f"SUV: {self.make} {self.model}\nRental Price: ${self.rental_price:.2f}\n"


class Truck(Vehicle):
    def __init__(self, make, model, rental_price):
        super().__init__(make, model, rental_price)

    def display_details(self):
        return f"Truck: {self.make} {self.model}\nRental Price: ${self.rental_price:.2f}\n"


class RentalReservation:
    def __init__(self, customer, vehicle, start_date, end_date):
        self.customer = customer
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date

    def display_details(self):
        return f"Rental Reservation: {self.customer.name}\n{self.vehicle.display_details()}Start Date: {self.start_date}, \nEnd Date: {self.end_date}\n"


class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.rental_history = []

    def display_rental_history(self):
        for reservation in self.rental_history:
            print(reservation.display_details())


def display_details(obj):
    print(obj.display_details())


car = Car("Audi", "R8", 500)
suv = SUV("Nissan", "Patrol", 600)
truck = Truck("Mercedes", "Daimler", 750)

customer1 = Customer("Hnery Cavill", "henryissupermana@example.com")
customer2 = Customer("Hugh Jackman", "loganisawesome@example.com")

reservation1 = RentalReservation(customer1, car, "01/09/23", "05/09/23")
reservation2 = RentalReservation(customer2, suv, "10/09/23", "15/09/23")
reservation3 = RentalReservation(customer1, truck, "20/09/23", "25/09/23")

customer1.rental_history.append(reservation1)
customer2.rental_history.append(reservation2)
customer1.rental_history.append(reservation3)

display_details(car)
display_details(suv)
display_details(truck)
display_details(reservation1)
display_details(reservation2)
display_details(reservation3)

customer1.display_rental_history()
customer2.display_rental_history()
