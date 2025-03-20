'''
Модуль для создания базы знаний из документации, взятой из сайта.
В файле listoflinks.txt записаны ссылки на статьи из сайта https://www.promptingguide.ai
С помощью библиотеки BeautifulSoup распарсивает страницу и записываем словарь.
После этого формирует JSON-файл, который будет нашей базой знаний.
'''
from bs4 import BeautifulSoup
import json
import requests


# Чтение списка ссылок из файла
def read_links_list(list):
    with open("listoflinks.txt", "r", encoding='UTF-8') as f:
        for line in f:
            list.append(line)

# Парсинг страницы сайта по ссылке, возвращает словарь для дальнейшей записи в json
def parse_page(url):
    response = requests.get(url)
    print(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Найти заголовок станицы и привести его к нужному виду
    title = soup.find('title').text
    title = title.replace("| Prompt Engineering Guide ", "")

    # Найти все элементы с тегом <main>
    content_str = ''
    reviews = soup.find('main')

    for review in reviews.find_all(['h2', 'p', 'pre']):
        content_str += review.text + ' '

    return {'title' : title, 'content': content_str}


# Запись данных в json-файл
def write_data(links_list):
    try:
        with open('data.json', 'w', encoding='UTF-8') as file:
            file.write("[\n")
            for i, item in enumerate(links_list):            
                json.dump(parse_page(item.strip()), file, ensure_ascii=False, indent=4)
                if(i != len(links_list)-1):
                    file.write(",\n")
            file.write("\n]")
    except:
        print("Ошибка записи в json-файл.")


if __name__ == "__main__":
    # Список ссылок
    links_list = []

    read_links_list(links_list)  
    write_data(links_list)