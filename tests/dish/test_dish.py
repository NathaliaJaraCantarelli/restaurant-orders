import pytest
from src.models.ingredient import Ingredient
from src.models.dish import Dish  # noqa: F401, E261, E501


# Req 2
def test_dish():
    bacon = Ingredient("bacon")
    bacon_quantity = 7

    sainduiche = "Sainduiche"
    saind_price = 5.00

    pastel = "Pastel"
    pastel_price = 3.50

    saind_dish = Dish(sainduiche, saind_price)
    pastel_dish = Dish(pastel, pastel_price)

    assert saind_dish.name == sainduiche
    assert saind_dish.__hash__() == saind_dish.__hash__()
    assert saind_dish.__hash__() != pastel_dish.__hash__()

    assert saind_dish == saind_dish

    assert repr(saind_dish) == f"Dish('{sainduiche}', R${saind_price:.2f})"

    with pytest.raises(TypeError):
        assert Dish(sainduiche, "1")
    with pytest.raises(ValueError):
        assert Dish(sainduiche, 0)

    saind_dish.add_ingredient_dependency(bacon, bacon_quantity)
    assert saind_dish.recipe.get(bacon) == bacon_quantity
    assert saind_dish.get_ingredients() == {bacon}

    assert saind_dish.get_restrictions() == bacon.restrictions
