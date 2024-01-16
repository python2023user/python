from food import Food

class Fruit(Food):
    def __init__(self, name, expiration_date):
        super().__init__(expiration_date)
        self.name = name

lemons = Fruit("lemons", "23.03.2024")
print(f"Fruit name: {lemons.name}\nExpiritation date: {lemons.expiritation_date}")