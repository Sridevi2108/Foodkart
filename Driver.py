# Import classes from their respective files
from User import User
from Restaurant import Restaurant
from Order import Order


class Driver:

    @staticmethod
    def run():
        while True:
            print("\n1. Register User")
            print("2. Login User")
            print("3. Register Restaurant")
            print("4. Show Restaurants (by price/rating)")
            print("5. Place Order")
            print("6. Rate Restaurant")
            print("7. Show Order History")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                # Register User
                name = input("Enter name: ")
                gender = input("Enter gender (M/F): ")
                phone_number = input("Enter phone number: ")
                pincode = input("Enter pincode: ")
                User.register_user(name, gender, phone_number, pincode)

            elif choice == "2":
                # Login User
                phone_number = input("Enter phone number to login: ")
                User.login_user(phone_number)

            elif choice == "3":
                # Register Restaurant
                if not User.logged_in_user:
                    print("Please login first.")
                else:
                    restaurant_name = input("Enter restaurant name: ")
                    serviceable_pincodes = input("Enter serviceable pincodes (separate by /): ")
                    food_item = input("Enter food item name: ")
                    price = float(input("Enter food item price: "))
                    quantity = int(input("Enter initial quantity: "))
                    Restaurant.register_restaurant(restaurant_name, serviceable_pincodes, food_item, price, quantity)

            elif choice == "4":
                # Show Restaurants
                if not User.logged_in_user:
                    print("Please login first.")
                else:
                    sort_by = input("Sort by (price/rating): ").strip().lower()
                    if sort_by not in ["price", "rating"]:
                        print("Invalid sorting option. Please choose 'price' or 'rating'.")
                    else:
                        Restaurant.show_restaurants(sort_by)

            elif choice == "5":
                # Place Order
                if not User.logged_in_user:
                    print("Please login first.")
                else:
                    restaurant_name = input("Enter restaurant name: ")
                    quantity = int(input("Enter quantity to order: "))
                    Order.place_order(restaurant_name, quantity)

            elif choice == "6":
                # Rate Restaurant
                if not User.logged_in_user:
                    print("Please login first.")
                else:
                    restaurant_name = input("Enter restaurant name to rate: ")
                    rating = int(input("Enter rating (1 to 5): "))
                    comment = input("Enter comment (optional): ")
                    if restaurant_name in Restaurant.restaurants:
                        Restaurant.restaurants[restaurant_name].add_rating(rating, comment)
                    else:
                        print("Restaurant not found.")

            elif choice == "7":
                # Show Order History
                if not User.logged_in_user:
                    print("Please login first.")
                else:
                    Order.show_order_history()

            elif choice == "8":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please select a valid option.")


# Run the driver class to simulate the application
if __name__ == "__main__":
    Driver.run()
