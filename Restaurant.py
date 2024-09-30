from User import User

class Restaurant:
    restaurants = {}

    def __init__(self, name, serviceable_pincodes, food_item, price, quantity):
        self.name = name
        self.serviceable_pincodes = serviceable_pincodes.split('/')  # Convert to list
        self.food_item = food_item
        self.price = price
        self.quantity = quantity
        self.ratings = []  # List of tuples: (rating, comment)
        Restaurant.restaurants[name] = self

    @classmethod
    def register_restaurant(cls, name, serviceable_pincodes, food_item, price, quantity):
        if name in cls.restaurants:
            print("Restaurant already exists!")
        else:
            cls(name, serviceable_pincodes, food_item, price, quantity)
            print(f"Restaurant {name} registered successfully!")

    def update_quantity(self, quantity_to_add):
        self.quantity += quantity_to_add
        print(f"{self.name}, {self.food_item} - {self.quantity}")

    def add_rating(self, rating, comment=None):
        self.ratings.append((rating, comment))
        print(f"Rating added for {self.name}")

    def get_average_rating(self):
        if not self.ratings:
            return 0  # No ratings yet
        return sum([x[0] for x in self.ratings]) / len(self.ratings)

    @classmethod
    def show_restaurants(cls, sort_by):
        if not User.logged_in_user:
            print("No user logged in.")
            return

        user_pincode = User.logged_in_user.pincode
        # Filter restaurants that serve the user's pincode and have non-zero quantity
        serviceable_restaurants = [
            r for r in cls.restaurants.values()
            if user_pincode in r.serviceable_pincodes and r.quantity > 0
        ]

        if not serviceable_restaurants:
            print("No serviceable restaurants available.")
            return

        # Sort based on user choice (price or rating)
        if sort_by == "price":
            serviceable_restaurants.sort(key=lambda r: r.price)
        elif sort_by == "rating":
            serviceable_restaurants.sort(
                key=lambda r: r.get_average_rating(), reverse=True
            )
        else:
            print("Invalid sorting option.")
            return

        # Display sorted restaurants
        for r in serviceable_restaurants:
            print(f"{r.name}, {r.food_item}, Price: {r.price}, Rating: {r.get_average_rating()}")

