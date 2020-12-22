"""
day21 - https://adventofcode.com/2020/day/21

--- Day 21: Allergen Assessment ---

* Part 1
a list of foods (your puzzle input), one food per line
Each line includes that food's ingredients list followed by some or all of the allergens the food contains.

- Each allergen is found in exactly one ingredient.
- Each ingredient contains zero or one allergen.
- Allergens aren't always marked
- When they are listed, the ingredient that contains each listed allergen will be 
    somewhere in the corresponding ingredients list

Determine which ingredients cannot possibly contain any of the allergens in your list.
How many times do any of those ingredients appear?
2162


* Part 2
Figure out which ingredient contains which allergen
Arrange the ingredients alphabetically by their allergen and separate them by commas 
 to produce your canonical dangerous ingredient list.

'dairy': ['lmzg'],
'fish': ['cxk'],
'nuts': ['bsqh'],
'peanuts': ['bdvmx']}
'sesame': ['cpbzbx'],
'shellfish': ['drbm'],
'soy': ['cfnt'],
'wheat': ['kqprv'],

lmzg,cxk,bsqh,bdvmx,cpbzbx,drbm,cfnt,kqprv

Note: Since I had already generated the list of suspects in part1, I did part 2 by hand in about 2 minutes

"""
def load_data():
    """
    Spent a long time coming up with this probably bad data structure:
    food {
        1: {
            ingredients: [],
            allergens: [],
        }
    }
    """
    all_ingredients = []
    all_allergens = []

    food = {}
    food_id = 0
    #datafile = 'input-day21-example'
    datafile = 'input-day21'
    with open(datafile, 'r') as input:
        for line in input:
            food_id += 1
            bits = line.strip().replace(")", "").split(" (contains ")
            ingredients = bits[0].split()
            allergens = bits[1].split(", ")
            food[food_id] = {}
            food[food_id]["ing"] = ingredients
            food[food_id]["all"] = allergens

            for ing in ingredients:
                all_ingredients.append(ing)

            for allergen in allergens:
                all_allergens.append(allergen)

    all_allergens.sort()
    all_ingredients.sort()

    uniq_allergens = set(all_allergens)
    uniq_ingredients = set(all_ingredients)

    return food, uniq_allergens, uniq_ingredients, all_ingredients


def part1(food, uniq_allergens, uniq_ingredients, all_ingredients):

    # generate a list of suspects for each allergen
    suspects = {}
    bad_ingredients = []
    for allergen in uniq_allergens:
        suspects[allergen] = []
        for ingredient in uniq_ingredients:
            if check_food(food, ingredient, allergen):
                suspects[allergen].append(ingredient)
                bad_ingredients.append(ingredient)

    print(f"suspects: {suspects}")

    #bad_ingredients = ['bsqh', 'cxk', 'cpbzbx', 'kqprv', 'lmzg', 'drbm', 'cfnt', 'bdvmx']

    good_ingredient_count = 0
    for ingredient in all_ingredients:
        if ingredient not in bad_ingredients:
            good_ingredient_count += 1
    return good_ingredient_count


def check_food(food, ingredient, allergen):
    """Need to find at least one allergen <-> ingredient match, and zero failed matches"""

    found_at_least_one_match = False
    for food_id in food:
        if allergen in food[food_id]["all"]:
            if ingredient not in food[food_id]["ing"]:
                return False
            else:
                found_at_least_one_match = True
    return found_at_least_one_match


if __name__ == '__main__':
    food, uniq_allergens, uniq_ingredients, all_ingredients = load_data()
    print(f"food: {food} \n")

    results1 = part1(food, uniq_allergens, uniq_ingredients, all_ingredients)
    print(f"\nPart 1 - {results1}")
