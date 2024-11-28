import re
from datetime import datetime

class Dish:
    def __init__(self, data):
        self.stud = re.findall(r'\b[A-Z][a-z]+_[A-Z]\.[A-Z]\.', data)[0]
        self.name = re.findall(r'"(.+?)"', data)[0]
        self.date_str = re.findall(r'\b(\d{2}\.\d{2}\.\d{4})\b', data)[0]
        self.date = datetime.strptime(self.date_str, '%d.%m.%Y')  # Преобразуем строку в объект datetime

    def __str__(self):
        return f'{self.name} - {self.date_str} - {self.stud}'

class MainTask:
    def __init__(self, stud_list):
        self.stud_list = []
        for data in stud_list:
            self.stud_list.append(Dish(data))

    def print_stud_list(self, dish_name):
        filtered_dishes = self.get_students_by_dish(dish_name)
        if filtered_dishes:
            for stud in filtered_dishes:
                print(stud)
        else:
            print("Нет студентов с такой работой.")

    def get_students_by_dish(self, dish_name):
        filtered_dishes = [dish for dish in self.stud_list if dish.name == dish_name]
        sorted_dishes = sorted(filtered_dishes, key=lambda x: x.date)  # Сортируем по объекту datetime
        return sorted_dishes

def main():
    with open("test_data.txt", "r", encoding="utf-8") as file:
        data = file.readlines()

    dishes = MainTask(data)

    # Запрос у пользователя
    dish_name = input("Введите название работы: ")
    print(f"Студенты, сделавшие '{dish_name}':")
    dishes.print_stud_list(dish_name)

if __name__ == '__main__':
    main()