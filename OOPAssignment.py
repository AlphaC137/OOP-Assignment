# Part 1: Smartphone Class with Inheritance and Polymorphism

class Device:
    def __init__(self, brand, model, battery_percentage):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage

    def check_battery(self):
        print(f"Battery is at {self.battery_percentage}%.")

    def charge(self, charge_amount):
        self.battery_percentage += charge_amount
        if self.battery_percentage > 100:
            self.battery_percentage = 100
        print(f"{self.brand} {self.model} charged to {self.battery_percentage}%.")


# Smartphone class inheriting from Device
class Smartphone(Device):
    def __init__(self, brand, model, battery_percentage, phone_number):
        super().__init__(brand, model, battery_percentage)  # Initialize the parent class (Device)
        self.phone_number = phone_number

    def make_call(self, number):
        print(f"Calling {number} from {self.phone_number}...")

    def send_message(self, message, number):
        print(f"Sending message: '{message}' to {number}")


# Tablet class inheriting from Device (polymorphism challenge)
class Tablet(Device):
    def __init__(self, brand, model, battery_percentage, screen_size):
        super().__init__(brand, model, battery_percentage)
        self.screen_size = screen_size

    # Overriding the check_battery method for Tablet
    def check_battery(self):
        print(f"Tablet battery is at {self.battery_percentage}%, with a {self.screen_size} inch screen.")

    def browse_internet(self):
        print(f"Browsing the internet on {self.brand} {self.model} with a {self.screen_size} inch display.")


# Creating instances of Smartphone and Tablet
my_phone = Smartphone("Apple", "iPhone 14", 50, "123-456-7890")
my_tablet = Tablet("Samsung", "Galaxy Tab", 75, 10)

# Using the methods from both objects
print("\nSmartphone Actions:")
my_phone.make_call("987-654-3210")
my_phone.check_battery()
my_phone.charge(30)
my_phone.send_message("Hey, how are you?", "987-654-3210")

print("\nTablet Actions:")
my_tablet.browse_internet()
my_tablet.check_battery()
my_tablet.charge(20)
