import cianparser
import time
import csv
import random
import os

# Настройки парсинга
locations = ['Москва и Московская область', 'Москва']
rooms = range(1, 5)
start_page = 1
end_page = 88

# Создание директории для сохранения файлов
base_dir = 'parser/base'
os.makedirs(base_dir, exist_ok=True)

# Функция для сохранения данных в файл
def save_data(data, filename):
    with open(filename, 'w', newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

# Парсинг данных
for city in locations:
    for room_count in rooms:
        for page in range(start_page, end_page + 1):
            parser = cianparser.CianParser(location=city)
            data = parser.get_flats(
                deal_type="sale", rooms=room_count,
                with_saving_csv=False,
                additional_settings={"start_page":page, "end_page":page}
            )

            if data:
                filename = f'{base_dir}/base_{city}_{room_count}_{page}.csv'
                save_data(data, filename)
                print(f"Данные для {city}, {room_count} комнат, страница {page} сохранены в {filename}")

            time.sleep(random.randint(5, 10))
