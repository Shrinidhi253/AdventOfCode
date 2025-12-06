def get_num_fresh_ingredients(intervals, available_ingredients):
    fresh_ingredients = []
    num_fresh_ingredients = 0

    for lower_limit, upper_limit in intervals:
        for ingredient in available_ingredients:
            if (
                ingredient >= lower_limit and 
                ingredient <= upper_limit and 
                ingredient not in fresh_ingredients
            ):
                fresh_ingredients.append(ingredient)
                num_fresh_ingredients += 1

    return num_fresh_ingredients

def main():
    data = ""

    with open("src/2025/day05/day05_ingredients_data.txt") as file:
        data = file.read()
        
    intervals_str, ingredients_str = data.split("\n\n")
    intervals = intervals_str.split("\n")
    ingredients = ingredients_str.split("\n")

    for i in range(len(intervals)):
        lower_limit, upper_limit = intervals[i].split("-")
        intervals[i] = (int(lower_limit), int(upper_limit))

    for i in range(len(ingredients)):
        ingredients[i] = int(ingredients[i])

    num_fresh_ingredients = get_num_fresh_ingredients(intervals, ingredients)

    print("Num fresh ingredients:", num_fresh_ingredients)

if __name__ == "__main__":
    main()
