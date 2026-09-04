"""
Codewars Kata: Pete, the baker (5 kyu)
Link: https://www.codewars.com/kata/525c65e51bf619685c000059

Description:
Pete likes to bake some cakes. He has some recipes and ingredients.
Unfortunately he is not good in maths. Can you help him to find out,
how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available
ingredients (object) and returns the maximum number of cakes Pete can bake (integer).
Ingredients that are not present in the objects, can be considered as 0.
"""


def cakes(recipe: dict, available: dict) -> int:
    minimum_cakes = float("inf")
    for element in recipe:
        substance = available.get(element, 0) // recipe[element]
        if substance == 0:
            return 0
        if substance < minimum_cakes:
            minimum_cakes = substance
    return minimum_cakes


if __name__ == "__main__":
    # Test cases
    recipe_1 = {"flour": 500, "sugar": 200, "eggs": 1}
    available_1 = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    print(cakes(recipe_1, available_1))  # 2

    recipe_2 = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available_2 = {"sugar": 500, "flour": 2000, "milk": 2000}
    print(cakes(recipe_2, available_2))  # 0
