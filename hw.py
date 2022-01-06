from pprint import pprint
from decor import decorator

def get_cook_book(file_name):
    cook_book = dict()
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            dish_name = line.strip()
            counter = int(file.readline())
            temp_list = []
            cook_book[dish_name] = temp_list

            for item in range(counter):
                ingredient_name, quantity, measure = file.readline().split('|')
                temp_list.append(
                    {'Название ингридиента': ingredient_name, 'Количество': quantity, 'Ед. измерения': measure})

            file.readline()

    return cook_book


cook_book = get_cook_book('recipes.txt')


@decorator
def get_shop_list_by_dishes(dishes, person_count, cook_book):
    menu = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                new_shop_list_item = dict(ingredient)
                dishes = []
                dishes.append(dishes)
                guests_menu = []
                guests_menu = get_cook_book('recipes.txt')[dish]
                for element in guests_menu:
                    menu.setdefault(element['Название ингридиента'], element)
                    del element['Название ингридиента']
                    a = int(element['Количество'])
                    quantity = a * person_count
                    element['Количество'] = quantity
    return menu




# pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 4, cook_book))
