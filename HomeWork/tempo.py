from pprint import pprint


def to_list_ingrid(a, b):
    for i in range(a, b):
        ingrid = {
                        'product': cook_book[i][0],
                        'quantity': cook_book[i][1],
                        'unit': cook_book[i][2]
                    }
        ingridient.append(ingrid)
        # print(ingridient)
    return ingridient


# dishes = []
ingridients = []
ingridient = []
# resipe = {}
# count = []

with open('2_1_cook_book.txt', 'r') as cook:
    cook_book = [line.strip().split(' | ') for line in cook]
# for i in range(len(cook_book)):
#     if len(cook_book[i][0]) == 1:
#         count.append(int(cook_book[i][0]))

ingridients.append(to_list_ingrid(2, 4))
pprint(ingridients)
ingridients.append(to_list_ingrid(7, 10))
pprint(ingridients)





