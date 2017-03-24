import yaml
import xml
import xml.etree.ElementTree as et
import csv
from pprint import pprint

# with open('godfather.yml') as godfather_file:
#     movie = yaml.load(godfather_file)
#     # pprint(movie)
#
#
# movie_xml = et.parse("godfather.xml")
# root = movie_xml.getroot()
# for e in movie_xml.iter():
#     # print(e.tag, e.attrib, e.text)


# with open("godfather.csv") as csv_god:
#     csv_movie = csv.reader(csv_god, delimiter=';')
#     for row in csv_movie:
        # print(row)

# with open("godfather.csv") as csv_god:
#     csv_movie = csv.DictReader(csv_god, delimiter=';')
#     for row in csv_movie:
#         print(row)

with open('cook_book.yml') as cook:
    cook_book = yaml.load(cook)

    for dishes in cook_book:
        pprint(cook_book)