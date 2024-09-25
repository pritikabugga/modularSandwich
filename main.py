import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

resources = data.resources
recipes = data.recipes
maker = SandwichMaker(resources)
cashier = Cashier()

def main():
    size = input("Choose sandwich size (small, medium, large): ").lower()

    if size in recipes and maker.check_resources(recipes[size]["ingredients"]):
        cost = recipes[size]['cost']
        print(f"Cost: ${cost:.2f}")
        if cashier.transaction_result(cashier.process_coins(), cost):
            maker.make_sandwich(size, recipes[size]["ingredients"])
            print(f"{size.capitalize()} sandwich served!")
        else:
            print("Insufficient funds.")
    else:
        print("Unavailable sandwich or insufficient resources.")

if __name__ == "__main__":
    main()
