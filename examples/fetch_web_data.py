import os

import requests
from bs4 import BeautifulSoup

import json

from config import data_dir

class FetchWebData:

    def fetch_text(self):
        URL='https://novinmarket.com/'
        req = requests.get(url=URL)
        soup = BeautifulSoup(req.text, 'html.parser')

        div = soup.find('div' , class_ ='moreParagraphs')
        text = div.find('p').text

        file_path = os.path.join(data_dir, 'data.txt')

        with open(file = file_path, mode='w', encoding='utf-8') as file:
            file.write(text)
        return    file_path

    def fetch_json(self):
        latitude = 52.512604
        longitude = 13.419517 

        params = {'latitude':latitude , 'longitude': longitude , 'current_weather': 'true' }
        url = 'https://api.open-meteo.com/v1/forecast'

        result = requests.get(params=params, url=url)

        file_path = os.path.join(data_dir, 'data.json')
        with open(file=file_path, encoding='utf-8', mode='w') as file:
            json.dump(result.json(),file, ensure_ascii=False, indent=4)

        return(file_path)

    def fetch_csv(self):
        URL= 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
        req = requests.get(url=URL)

        file_path = os.path.join(data_dir, 'data.csv')

        with open(file=file_path, mode='w') as file:
            file.write(req.text)

        return file_path    


# if __name__ == "__main__":
#     fetcher = FetchWebData()
#     fetcher.fetch_text()
#     fetcher.fetch_json()
#     fetcher.fetch_csv()

    






 
