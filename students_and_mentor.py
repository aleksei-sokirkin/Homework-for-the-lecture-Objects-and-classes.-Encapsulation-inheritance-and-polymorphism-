class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturers(self, lecturer, course, grade):
        """Выставление оценок лекторам."""
        if isinstance(lecturer, 
                      Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.course_grades:
                lecturer.course_grades[course] += [grade]
            else:
                lecturer.course_grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        """Средняя оценка студентам за домашнее задание"""
        for value in self.grades.values():
            сourse_sum = 0
            for grade in value:
                сourse_sum += grade     
            average_grade = сourse_sum/len(value)
            return average_grade

    def __lt__(self, student):
        if not isinstance(student, Student):
            print("Ошибка")
            return
        return student.average_grade() > self.average_grade()

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade()}\n'
                f'Курсы в процессе изучения:{", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_grades = {}

    def average_grade(self):
        """Средняя оценка лекторам"""
        for value in self.course_grades.values():
            course_sum = 0
            for grade in value:
                course_sum += grade     
            average_grade = course_sum/len(value)
            return average_grade

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade()}')

    def __lt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            print("Ошибка")
            return
        return lecturer.average_grade() > self.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """Выставление оценок студентам."""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')


def mid_grades_lecturer(lecturers, course):
    average_rating = 0
    for lecturer in lecturers:
        if course in lecturer.course_grades.keys():
            lecturer_average_score = 0
            for grades in lecturer.course_grades[course]:
                lecturer_average_score += grades
            average_rating = lecturer_average_score / len(lecturer.course_grades[course])    
        return f"Средняя оценка за курс {course} у всех студентов {average_rating}"


def mid_grades_student(students, course):
    overall_student_rating = 0
    for listener in students:
        if course in listener.grades.keys():
            average_student_score = 0
            for grades in listener.grades[course]:
                average_student_score += grades
            overall_student_rating = average_student_score / len(listener.grades[course])    
        return f"Средняя оценка за курс {course} у всех студентов {overall_student_rating}"


first_student = Student('Ruoy', 'Eman', 'your_gender')
second_student = Student('Rio', 'Emin', 'your_gender')
first_student.courses_in_progress += ['Python', 'JavaScript']
first_student.finished_courses += ['Exel']
second_student.courses_in_progress += ['Python', 'C+']
second_student.finished_courses += ['Exel']
students = [first_student, second_student]

first_reviewer = Reviewer('Some', 'Buddy')
first_reviewer.courses_attached += ['Python', 'JavaScript']
second_reviewer = Reviewer('Rem', 'Beddi')
second_reviewer.courses_attached += ['Python', 'C+']

first_lecturer = Lecturer('Tim', 'Tert')
first_lecturer.courses_attached = ['Python', 'Java']
second_lecturer = Lecturer('Yer', 'Upd')
second_lecturer.courses_attached = ['Python', 'Java']
lecturers = [first_lecturer, second_lecturer]

first_student.rate_lecturers(first_lecturer, 'Python', 8)
first_student.rate_lecturers(second_lecturer, 'Python', 9)
second_student.rate_lecturers(first_lecturer, 'Python', 7)
second_student.rate_lecturers(second_lecturer, 'Python', 8)

first_reviewer.rate_hw(first_student, 'Python', 6)
first_reviewer.rate_hw(second_student, 'Python', 9)
second_reviewer.rate_hw(first_student, 'Python', 5)
second_reviewer.rate_hw(second_student, 'Python', 8)

print(second_student)
print(first_reviewer)
print(second_lecturer)
print(second_student > first_student)
print(second_lecturer > first_lecturer)

print(mid_grades_student(students, 'Python'))
print(mid_grades_lecturer(lecturers, 'Python'))