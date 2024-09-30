class User:
    users = {}
    logged_in_user = None

    def __init__(self, name, gender, phone_number, pincode):
        self.name = name
        self.gender = gender
        self.phone_number = phone_number
        self.pincode = pincode
        User.users[phone_number] = self

    @classmethod
    def register_user(cls, name, gender, phone_number, pincode):
        if phone_number in cls.users:
            print("User already exists!")
        else:
            cls(name, gender, phone_number, pincode)
            print(f"User {name} registered successfully!")

    @classmethod
    def login_user(cls, phone_number):
        if phone_number in cls.users:
            cls.logged_in_user = cls.users[phone_number]
            print(f"User {cls.logged_in_user.name} logged in!")
        else:
            print("User not found!")
