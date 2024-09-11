"""
Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.
Perform the following tasks now:
 Now add items to the menu.
 Make table reservations.
 Take customer orders.
 Print the menu.
 Print table reservations.
 Print customer orders.

"""

class Restaurant:
  def __init__(self, menu_items, book_table, customer_orders):
    self.menu_items = menu_items
    self.book_table = book_table
    self.customer_orders = customer_orders
  def add_item_to_menu(self, item):
    self.menu_items.append(item)
    
  def book_tables(self, table_number):
    self.book_table.append(table_number)
    
  def customer_order(self, order):
    self.customer_orders.append(order)

  def print_menu(self):
    print("Menu: " + str(self.menu_items))

  def print_table_reservations(self):
    print("Table Reservations: " + str(self.book_table))

  def print_customer_orders(self):
    print("Customer Orders: " + str(self.customer_orders))


# Example usage:
menu_items = ["Pizza", "Burger", "Salad"]
book_table = [1, 2, 3]
customer_orders = ["Pizza", "Burger"]
restaurant = Restaurant(menu_items, book_table, customer_orders)
restaurant.add_item_to_menu("Sushi")
restaurant.book_tables(4)
restaurant.customer_order("Salad")

restaurant.print_menu()
