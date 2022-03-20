

def get_recipe_price(dic, optionals=None, **ingredients):
    """
    The function calculate the price we need to pay for the ingredients and amount that we want to pay
    example: get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100) return 54
    :param dic: dictionary of ingredients prices.
    :param optionals: ingredients that we don't want to buy.
    :param ingredients: that we want to buy and the amount.
    :return: price of all the ingredients we wanted to buy
    """
    if optionals == None:
        optionals = []
    if not ingredients:
        return 0
    price = 0
    for ingredient, amount in ingredients.items():
        if ingredient not in optionals:
            price += dic[ingredient] * amount//100
    return price


print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))

print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))

print(get_recipe_price({}))