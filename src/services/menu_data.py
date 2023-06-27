import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self._load_menu(source_path)

    def _load_menu(self, source_path: str):
        with open(source_path, "r") as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                dish = row["dish"]
                price = float(row["price"])
                ingredient = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])

                new_ing = Ingredient(ingredient)
                new_dish = self._check_dish(dish, price)
                new_dish.add_ingredient_dependency(new_ing, recipe_amount)

    def _check_dish(self, dish: str, price: float) -> Dish:
        for self_dish in self.dishes:
            if self_dish.name == dish and self_dish.price == price:
                return self_dish

        create_dish = Dish(dish, price)
        self.dishes.add(create_dish)
        return create_dish
