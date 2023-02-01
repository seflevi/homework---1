class Student:
    def __init__(self, name, surname):

        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def __str__(self):

        grades_count = 0
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = round(sum(map(sum, self.grades.values())) / grades_count, 2)
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_rating}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_str}\n' \
              f'Завершенные курсы: {finished_courses_str}'
        return res

    def rate_hw(self, lecturer, course, grade):

        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):

        if not isinstance(other, Student):
            print('Такое сравнение неправильное')
            return
        return self.average_rating < other.average_rating

class Mentor:
    def __init__(self, name, surname):

        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):

    def __init__(self, name, surname):

        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):

        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = round(sum(map(sum, self.grades.values())) / grades_count, 2)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return res

    def __lt__(self, other):

        if not isinstance(other, Lecturer):
            print('Такое сравнение неправильное')
            return
        return self.average_rating < other.average_rating


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):

        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):

        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
student_1 = Student('Mark', 'Ivanov')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Igor', 'Yakovlev')
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Maxim', 'Sidorov')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']

lecturer_1 = Lecturer('Fedor', 'Smirnov')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Ivan', 'Fedorov')
lecturer_2.courses_attached += ['Git']

lecturer_3 = Lecturer('Artem', 'Ageev')
lecturer_3.courses_attached += ['Python']

reviewer_1 = Reviewer('Egor', 'Shalenko')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']

reviewer_2 = Reviewer('Semen', 'Agapov')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']

student_1.rate_hw(lecturer_1, 'Python', 9)
student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 8)

student_1.rate_hw(lecturer_2, 'Python', 8)
student_1.rate_hw(lecturer_2, 'Python', 7)
student_1.rate_hw(lecturer_2, 'Python', 9)

student_1.rate_hw(lecturer_1, 'Python', 7)
student_1.rate_hw(lecturer_1, 'Python', 6)
student_1.rate_hw(lecturer_1, 'Python', 10)

student_2.rate_hw(lecturer_2, 'Git', 5)
student_2.rate_hw(lecturer_2, 'Git', 3)
student_2.rate_hw(lecturer_2, 'Git', 10)

student_3.rate_hw(lecturer_3, 'Python', 8)
student_3.rate_hw(lecturer_3, 'Python', 4)
student_3.rate_hw(lecturer_3, 'Python', 9)

reviewer_1.rate_hw(student_1, 'Python', 6)
reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_1, 'Python', 9)

reviewer_2.rate_hw(student_2, 'Git', 5)
reviewer_2.rate_hw(student_2, 'Git', 4)
reviewer_2.rate_hw(student_2, 'Git', 10)

reviewer_2.rate_hw(student_3, 'Python', 7)
reviewer_2.rate_hw(student_3, 'Python', 5)
reviewer_2.rate_hw(student_3, 'Python', 8)
reviewer_2.rate_hw(student_3, 'Python', 10)
reviewer_2.rate_hw(student_3, 'Python', 6)
reviewer_2.rate_hw(student_3, 'Python', 5)

print(f'Перечень студентов:\n{student_1}\n{student_2}\n{student_3}')

print(f'Перечень лекторов:\n{lecturer_1}\n{lecturer_2}\n{lecturer_3}')

print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')

print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{lecturer_1.name} {lecturer_1.surname} < {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 > lecturer_2}')

student_list = [student_1, student_2, student_3]

lecturer_list = [lecturer_1, lecturer_2, lecturer_3]

def student_rating(student_list, course_name):

    sum_all = 0
    count_all = 0
    for stud in student_list:
       if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = round(sum_all / count_all, 2)
    return average_for_all

def lecturer_rating(lecturer_list, course_name):

    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = round(sum_all / count_all, 2)
    return average_for_all

print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")

print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")

print(f"Средняя оценка для всех студентов по курсу {'Git'}: {student_rating(student_list, 'Git')}")

print(f"Средняя оценка для всех лекторов по курсу {'Git'}: {lecturer_rating(lecturer_list, 'Git')}")