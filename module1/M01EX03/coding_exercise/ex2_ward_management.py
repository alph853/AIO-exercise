from typing import List
from abc import ABC, abstractmethod


JOBS_TITLE = ["Student", "Teacher", "Doctor"]


class Person:
    def __init__(self, name: str, yob: int):
        self.name = name
        self.yob = yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self.grade = grade

    def __str__(self):
        return "Student"

    def describe(self):
        print(f"Student: {self.name} ({self.yob}) - grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self.subject = subject

    def __str__(self):
        return "Teacher"

    def describe(self):
        print(f"Teacher: {self.name} ({self.yob}) - subject: {self.subject}")


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialization: str):
        super().__init__(name, yob)
        self.specialization = specialization

    def __str__(self):
        return "Doctor"

    def describe(self):
        print(
            f"Doctor: {self.name} ({self.yob}) - specialization: {self.specialization}")


class Ward:
    def __init__(self, name: str):
        self.citizen_list: List[Person] = []
        self.ward_name = name
        self.job_distribution = {job: 0 for job in JOBS_TITLE}

    def add_person(self, person: Person):
        self.citizen_list.append(person)
        self.job_distribution[str(person)] += 1

    def describe(self):
        print(f"Ward: {self.ward_name}")
        for person in self.citizen_list:
            person.describe()

    def count_doctor(self):
        return self.job_distribution["Doctor"]

    def sort_age(self):
        self.citizen_list.sort(key=lambda x: x.yob, reverse=True)

    def compute_average_teacher_age(self):
        return sum([teacher.yob for teacher in self.citizen_list if isinstance(teacher, Teacher)]) / self.job_distribution["Teacher"]


def ex2():
    ward = Ward("Ward 1")
    student1 = Student("Alice", 2000, "A")
    student2 = Student("Bob", 2001, "B")
    teacher1 = Teacher("Charlie", 1980, "Math")
    teacher2 = Teacher("David", 1985, "Physics")
    doctor1 = Doctor("Eve", 1970, "Cardiology")
    doctor2 = Doctor("Frank", 1975, "Dentistry")

    ward.add_person(student1)
    ward.add_person(student2)
    ward.add_person(teacher1)
    ward.add_person(teacher2)
    ward.add_person(doctor1)
    ward.add_person(doctor2)

    ward.describe()

    print('-'*50)
    print('After sorting by age:')
    print('-'*50)

    ward.sort_age()
    ward.describe()

    print(f'Number of doctors: {ward.count_doctor()}')
    print(
        f'Average year of birth (teachers): {ward.compute_average_teacher_age()}')
