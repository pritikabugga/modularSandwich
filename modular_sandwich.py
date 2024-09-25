class SandwichMaker:
    def __init__(self, resources):
        self.resources = resources

    def check_resources(self, ingredients):
        return all(self.resources[item] >= amount for item, amount in ingredients.items())

    def make_sandwich(self, size, ingredients):
        for item, amount in ingredients.items():
            self.resources[item] -= amount
        print(f"{size.capitalize()} sandwich made!")
