# Parent class
class Smartphone:
    def __init__(self, brand, model, battery):
        # Public attributes
        self.brand = brand
        self.model = model
        # Private attribute (encapsulation)
        self.__battery = battery  

    # Method to show phone details
    def show_info(self):
        return f"{self.brand} {self.model} | Battery: {self.__battery}%"

    # Getter for battery
    def get_battery(self):
        return self.__battery

    # Method to use battery
    def use_phone(self, hours):
        drain = hours * 5
        if self.__battery - drain >= 0:
            self.__battery -= drain
            print(f"📱 Used for {hours}h, battery now {self.__battery}%")
        else:
            print("⚠️ Battery too low! Please charge.")

    # Method to charge battery
    def charge(self, amount):
        self.__battery = min(100, self.__battery + amount)
        print(f"🔋 Charging... Battery at {self.__battery}%")


# Child class (Inheritance + Polymorphism)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery, gpu_power):
        super().__init__(brand, model, battery)
        self.gpu_power = gpu_power  # extra attribute

    # Override (Polymorphism)
    def use_phone(self, hours):
        # Gaming drains battery faster
        drain = hours * 15  
        if self.get_battery() - drain >= 0:
            # Using parent method with modification
            print(f"🎮 Gaming for {hours}h on {self.brand} {self.model}")
            super().use_phone(hours * 3)  # stronger drain effect
        else:
            print("⚠️ Battery too low for gaming!")


# ---- TESTING ----
# Create objects
phone1 = Smartphone("Samsung", "Galaxy S21", 80)
game_phone = GamingPhone("Asus", "ROG Phone 6", 90, "Ultra GPU")

# Use parent class
print(phone1.show_info())
phone1.use_phone(3)
phone1.charge(15)

# Use child class with polymorphism
print(game_phone.show_info())
game_phone.use_phone(2)  # Gaming drains more battery
