import pytest
from src.models.ingredient import Ingredient
from src.models.dish import Dish  # noqa: F401, E261, E501


# Req 2
def test_dish():
    bacon = Ingredient("bacon")
    bacon_quantity = 7

    sainduiche = "Sainduiche"
    sainduiche_price = 5.00

    pastel = "Pastel"
    pastel_price = 3.50

    sainduiche_dish = Dish(sainduiche, sainduiche_price)
    pastel_dish = Dish(pastel, pastel_price)

    assert sainduiche_dish.name == sainduiche
    assert sainduiche_dish.__hash__() == sainduiche_dish.__hash__()
    assert sainduiche_dish.__hash__() != pastel_dish.__hash__()

    assert sainduiche_dish == sainduiche_dish

    assert repr(sainduiche_dish) == f"Dish('{sainduiche}', R${sainduiche_price:.2f})"

    with pytest.raises(TypeError):
        assert Dish(sainduiche, "1")
    with pytest.raises(ValueError):
        assert Dish(sainduiche, 0)

    sainduiche_dish.add_ingredient_dependency(bacon, bacon_quantity)
    assert sainduiche_dish.recipe.get(bacon) == bacon_quantity
    assert sainduiche_dish.get_ingredients() == {bacon}

    assert sainduiche_dish.get_restrictions() == bacon.restrictions