# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_level):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level

    def charge(self, charge_amount):
        self.battery_level += charge_amount
        print(f"{self.brand} {self.model} is charging. Battery level: {self.battery_level}%")

    def make_call(self, number):
        if self.battery_level > 0:
            print(f"Calling {number} from {self.brand} {self.model}...")
            self.battery_level -= 5  # Assuming call drains battery by 5%
        else:
            print("Battery too low to make a call!")

# Subclass: AdvancedSmartphone
class AdvancedSmartphone(Smartphone):
    def __init__(self, brand, model, battery_level, camera_resolution):
        super().__init__(brand, model, battery_level)
        self.camera_resolution = camera_resolution

    def take_photo(self):
        print(f"Taking a photo with {self.camera_resolution}MP camera!")

# Creating instances
phone1 = Smartphone("Apple", "iPhone 14", 50)
phone2 = AdvancedSmartphone("Samsung", "Galaxy S22", 70, 108)

# Using methods
phone1.charge(20)
phone1.make_call("123-456-7890")

phone2.take_photo()
phone2.make_call("987-654-3210")
