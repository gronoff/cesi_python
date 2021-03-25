import requests
import json
import os.path


class OpenFoodFactApi:
    def __init__(self):
        self.products = []

    def __checkCacheFile(self):
        return True if os.path.isfile('openFoodFactCache.txt') else False

    def __createCacheFile(self):
        open("openFoodFactCache.txt", "x")

    def getAll(self):
        return requests.get('https://fr.openfoodfacts.org/cgi/search.pl?json=True&action=process&page_size=50&sort_by=unique_scans_n&tagtype_0=status&tag_contains_0=without&tag_0=to-be-completed&tagtype_1=status&tag_contains_1=without&tag_1=to-be-checked&fields=code%2Cproduct_name%2Ccategories&page=0').json()

    def getOne(self, id):
        if not self.__checkCacheFile():
            self.__createCacheFile()
            product = requests.get(
                f'https://fr.openfoodfacts.org/api/v0/product/{id}.json').json()
            self.products.append(product)
            f = open("openFoodFactCache.txt", "a")
            f.write(json.dumps(self.products))
            return product


toto = OpenFoodFactApi()

print(toto.getAll())
print(toto.getOne(3451790988677))
