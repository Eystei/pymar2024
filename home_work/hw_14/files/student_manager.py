import datetime
from loguru import logger

STUDENTS_DATA = [
    "Pikachu, Group 1, 5",
    "Charmander, Group 1, 4",
    "Bulbasaur, Group 2, 3",
    "Squirtle, Group 2, 4",
    "Eevee, Group 1, 5"
]

logger.add("student_manager.log", rotation="10 MB")


class StudentManager:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def check_and_create_file(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                if file.readline() == "":
                    logger.info(f"File '{self.filename}' empty. Write init data.")
                    self.write_initial_students_data()
                else:
                    logger.info(f"File '{self.filename}' already exists with data.")
        except FileNotFoundError:
            logger.warning(f"File '{self.filename}' not exist. Create init data.")
            self.write_initial_students_data()

    def write_initial_students_data(self):
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                for student in STUDENTS_DATA:
                    file.write(student + "\n")
        except IOError as e:
            logger.error(f"Error create or write file: {e}")

    def load_students_from_file(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.students = file.readlines()
                if not self.students:
                    logger.warning(f"File '{self.filename}' empty.")
        except IOError as e:
            logger.error(f"Error reading from file: {e}")
            self.students = []

    def calculate_statistics(self):
        total_students = 0
        group_data = {}

        for student in self.students:
            parts = student.strip().split(", ")
            if len(parts) == 3:
                _, group, grade = parts
                grade = int(grade.split()[-1])
                group_name = group.split()[-1]

                if group_name not in group_data:
                    group_data[group_name] = {'count': 0, 'total_grade': 0}

                group_data[group_name]['count'] += 1
                group_data[group_name]['total_grade'] += grade
                total_students += 1

        group_averages = {k: v['total_grade'] / v['count'] for k, v in group_data.items()}

        return total_students, group_data, group_averages

    def append_statistics_to_file(self, total_students, group_data, group_avg):
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open(self.filename, 'a', encoding='utf-8') as file:
                file.write(f"\nDate: {time}\n")
                file.write(f"Number of students: {total_students}\n")
                for group, data in group_data.items():
                    file.write(f"Group {group}: {data['count']} students, "
                               f"Average grade: {group_avg[group]:.2f}\n")
        except IOError as e:
            logger.error(f"Error writing to file: {e}")

    def process_student_data(self):
        self.check_and_create_file()
        self.load_students_from_file()
        total_students, group_data, group_avg = self.calculate_statistics()
        self.append_statistics_to_file(total_students, group_data, group_avg)


if __name__ == "__main__":
    manager = StudentManager("students.txt")
    manager.process_student_data()
