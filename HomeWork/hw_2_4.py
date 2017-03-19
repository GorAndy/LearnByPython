# -*- coding: utf-8 -*-
import os.path
import glob


def list_of_files(path):
    files = glob.glob(os.path.join(path, "*.sql"))
    return files


def search_in_list(strict, list_files):
    for file in list_files:
        with open(file, encoding='utf8') as f:
            if strict in f.read():
                result_search.append(file)
    return result_search


path = './Migrations'
result_search = []

strict = input('Введите строку поиска: ')
search_before = search_in_list(strict, list_of_files(path))
print(search_before)
print('Total: ', len(search_before))

while True:
    strict = input('Введите строку поиска в результатах поиска: ')
    result_search = []
    search_after = search_in_list(strict, search_before)
    print(search_after)
    print('Total: ', len(search_after))
    search_before, search_after = search_after, []
