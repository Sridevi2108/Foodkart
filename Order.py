from Restaurant import Restaurant
from User import User
class Order:
    order_history = {}  # In-memory store for user orders

    def __init__(self, restaurant, quantity):
        self.restaurant = restaurant
        self.quantity = quantity
        Order.order_history.setdefault(User.logged_in_user.phone_number, []).append(self)

    @classmethod
    def place_order(cls, restaurant_name, quantity):
        if not User.logged_in_user:
            print("No user logged in.")
            return

        restaurant = Restaurant.restaurants.get(restaurant_name)
        if restaurant and restaurant.quantity >= quantity:
            restaurant.quantity -= quantity
            cls(restaurant_name, quantity)
            print(f"Order placed successfully from {restaurant_name}!")
        else:
            print(f"Cannot place order from {restaurant_name}")

    @classmethod
    def show_order_history(cls):
        if not User.logged_in_user:
            print("No user logged in.")
            return

        phone_number = User.logged_in_user.phone_number
        orders = cls.order_history.get(phone_number, [])

        if not orders:
            print(f"No orders found for user {User.logged_in_user.name}")
        else:
            for order in orders:
                print(f"Order from {order.restaurant} - Quantity: {order.quantity}")
