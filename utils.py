from bs4 import BeautifulSoup
import json


class Utils():

    def __init__(self):
        pass

    def extract_data(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        data_script = str(soup.find('script', {'id': 'data'}))
        data = json.loads(data_script[31:-10])
        return data

    def extract_post_text(self, data):
        text = ''
        document = data['document']

        for elem in document:
            if elem['e'] == 'par':
                for f in elem['c']:
                    if f['e'] == 'text':
                        text += f['t']
                text += '\n'
        return text

    # Извлекаем из всей информации только теги
    def extract_flair(self, data:list):
        flair = []
        for elem in data:
            if elem['type'] == 'text':
                tag = elem['text']
                flair.append(tag)
        return flair
