import yaml

def add_to(recipe):
    dish_recipe = {}
    name_dish = recipe[0]
    dish_recipe[name_dish] = []
    for ingridient in recipe[2::]:
        ingridient = ingridient.split('|')
        dish_recipe[name_dish].append({'ingridient_name': ingridient[0].strip(),\
                                       'quantity': int(ingridient[1]), 'measure': ingridient[2].strip()})
    return dish_recipe


def get_cook_book():
    recipe = []
    cook_book = {}
    with open('cook_book.yml', 'r') as cook:
        cook_book = yaml.load(cook)
        # for line in cook:
        #     line = line.strip()
        #     if not line:
        #         cook_book.update(add_to(recipe))
        #         recipe = []
        #     else:
        #         recipe.append(line)
        # cook_book.update(add_to(recipe))
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book()
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list = dict(ingridient)
            new_shop_list['quantity'] *= person_count
            if new_shop_list['ingridient_name'] not in shop_list:
                shop_list[new_shop_list['ingridient_name']] = new_shop_list
            else:
                shop_list[new_shop_list['ingridient_name']]['quantity'] += new_shop_list['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))


def create_shop_list():
    person_count = int(input('Введите количество едоков: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую):').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()