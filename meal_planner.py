from contents import pantry, recipes


def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """

    :param data:
    :param item:
    :param amount:
    :return:
    """

    data[item] = data.setdefault(item, 0) + amount


display_dict = {}

for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key


shopping_list = {}

while True:
    print("please choose your recipe")
    print("*************************")
    for key, value in display_dict.items():
        print(f"{key} {value}")
    choice = input(": ")
    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print("you have selected {}".format(selected_item))
        print("selecting ingredients")
        ingredients = recipes[selected_item]
        print(ingredients)
        for ingredient, amount_we_need in ingredients.items():
            amount_we_have = pantry.get(ingredient, 0)
            if amount_we_need <= amount_we_have:
                print(f"\t{ingredient} is in the pantry")
            else:
                quantity_to_buy = amount_we_need - amount_we_have
                print(f"\tyou need {quantity_to_buy} of {ingredient}")
                add_shopping_item(shopping_list, ingredient, quantity_to_buy)

for things in shopping_list.items():
    print(things)
