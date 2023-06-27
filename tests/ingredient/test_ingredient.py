from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    bacon = Ingredient('bacon')
    farinha = Ingredient('farinha')

    assert bacon.__hash__() == bacon.__hash__()
    assert bacon.__hash__() != farinha.__hash__()

    assert bacon == bacon
    assert repr(bacon) == "Ingredient('bacon')"
    assert bacon.name == 'bacon'
    assert farinha.restrictions == {Restriction.GLUTEN}
