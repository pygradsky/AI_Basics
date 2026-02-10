class Student:
    def __init__(self,
                 student_id,
                 surname, first_name, last_name,
                 birth_date,
                 address,
                 phone_number,
                 faculty,
                 course,
                 group,
                 average_score):

        self.student_id = student_id
        self.surname = surname
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.address = address
        self.phone_number = phone_number
        self.faculty = faculty
        self.course = course
        self.group = group
        self.average_score = average_score


    def get_student_id(self):
        return self.student_id

    def get_surname(self):
        return self.surname

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_birth_date(self):
        return self.birth_date

    def get_address(self):
        return self.address

    def get_phone_number(self):
        return self.phone_number

    def get_faculty(self):
        return self.faculty

    def get_course(self):
        return self.course

    def get_group(self):
        return self.group

    def get_average_score(self):
        return self.average_score

    def get_student_info(self):
        return f"ID студента: {self.student_id}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Имя: {self.first_name}\n" \
               f"Отчество: {self.last_name}\n" \
               f"Дата рождения: {self.birth_date}\n" \
               f"Адрес: {self.address}\n" \
               f"Номер телефона: {self.phone_number}\n" \
               f"Факультет: {self.faculty}\n" \
               f"Курс: {self.course}\n" \
               f"Группа: {self.group}\n" \
               f"Средний балл: {self.average_score}"


student1 = Student(1, "Smith", "John", "Doe", "01.01.2000", "123 Main St", "+1234567890", "Engineering", 2, "A", 4.5)
student2 = Student(2, "Johnson", "Jane", "Doe", "02.02.2001", "456 Elm St", "+0987654321", "Science", 3, "B", 4.8)
student3 = Student(3, "Brown", "Michael", "Smith", "03.03.2002", "789 Oak St", "+1122334455", "Arts", 1, "C", 4.2)


list_of_students = [student1, student2, student3]

# a)

faculty_input = input("Введите название факультета: ")
students_in_faculty = [student for student in list_of_students if student.get_faculty() == faculty_input]
print(f"Студенты факультета {faculty_input}: {students_in_faculty}")


# b)
course_input = input("Введите номер курса: ")
students_in_faculty_and_course = [student for student in list_of_students if student.get_faculty() == faculty_input and student.get_course() == int(course_input)]
print(f"Студенты факультета {faculty_input} и курса {course_input}: {students_in_faculty_and_course}")


# c)
# -


# d)
# -
