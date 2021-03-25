import requests
import json


class OpenFoodFactApi:
    def __init__(self):
        self.products = []

    def getAll(self):
        return requests.get('https://fr.openfoodfacts.org/cgi/search.pl?json=True&action=process&page_size=50&sort_by=unique_scans_n&tagtype_0=status&tag_contains_0=without&tag_0=to-be-completed&tagtype_1=status&tag_contains_1=without&tag_1=to-be-checked&fields=code%2Cproduct_name%2Ccategories&page=0').json()

    def getOne(self, id):
        return requests.get(f'https://fr.openfoodfacts.org/api/v0/product/{id}.json').json()


toto = OpenFoodFactApi()

print(toto.getAll())
print(toto.getOne(3451790988677))
