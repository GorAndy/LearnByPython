import json
from pprint import pprint
import chardet
import os


files = os.listdir()
file_json = filter(lambda x: x.endswith('.json'), files)
file_json_list = list(file_json)
encoding_file_list = []
sum_file = []
for file in file_json_list:
    with open(file, 'rb') as fj:
        fjs = fj.read()
        encoding_file_dict = chardet.detect(fjs)
        encoding_file_list.append(encoding_file_dict['encoding'])
file_encod = zip(file_json_list, encoding_file_list)
for file, encod in file_encod:
    with open(file, 'r', encoding=encod) as fjr:
        file_for_parsing = fjr.read().strip().split()
        sum_file.append(file_for_parsing)
counter = {}
for item in sum_file:
    for word in item:
        if len(word) > 6:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
top = sorted(counter.items(), key=lambda x: x[1], reverse=True)
top_ten = top[1:10]
pprint(top_ten)
