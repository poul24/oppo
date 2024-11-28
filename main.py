import re

dishes = []

class Dish:
    def __init__(self, data):
        self.stud = re.findall(r'\b[A-Z][a-z]+_[A-Z]\.[A-Z]\.', data)[0]
        self.name = re.findall(r'"(.+?)"', data)[0]
        self.date = re.findall(r'\b(\d{2}\.\d{2}\.\d{4})\b', data)[0]

    def __str__(self):
        return f'{self.name} - {self.date} - {self.stud}'


class MainTask:
    def __init__(self, stud_list):
        self.stud_list = []
        for data in stud_list:
            self.stud_list.append(Dish(data))

    def print_stud_list(self):
        for stud in self.stud_list:
            print(stud)

    def print_student_list(self, stud):
        filtered_students = []
        for student in self.student_list:
            if student.stud == stud:
                filtered_students.append(student)
        a = sorted(filtered_students, key=lambda student: student.date)
        for i in a:
            print(i.name)


if __name__ == '__main__':
    with open("test_data.txt", "r", encoding="utf-8") as file:
        data = file.readlines()

    dishes = MainTask(data)
    dishes.print_stud_list()

    Students.print_student_list("Salut")