class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Sveiks {self.name}!")
person1 = Person("Jānis", 36)
person1.greet()
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def greet(self):
        print(f"Sveiks {self.name} numur {self.student_id}!")
student1 = Student("Pēteris", 22, "223344")
student1.greet()
class Course:
    def __init__(self, nosaukums, saraksts):
        self.nosaukums = nosaukums
        self.saraksts = saraksts
        self.students = []
    def add_student(self, student):
            self.students.append(student)
          
    def list_students(self):
        for student in self.students:
            print(f"{student.name} ({student.student_id})")
    def list_students_with_grades(self):
        for student in self.students:
            print(f"{student.name} ({grade.grade})")
            
course1 = Course("Python", ["Jānis", "Kristers", "Anna"])
course1.add_student(student1)

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    def greet(self):
        print(f"Sveiks {self.name} jūs mācat {self.subject}!")
teacher1 = Teacher("Māris", 45, "Matemātika")
teacher1.greet()

class Library:
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums
    def remove_book(self, nosaukums):
        self.__del__(nosaukums)
#
lib1 = Library("Teletubiji")
lib2 = Library("Poters")
print(lib1.nosaukums)
del lib1
print(lib1.nosaukums)
#
class School:
     def __init__(self, name):
        self.name = name
        self.kurss = []
     def add_course(self, title):
        self.kurss.append(title)
     def list_courses(self):
        if self.kurss:
            print(f"Skolas {self.name} piedāvātie kursi:")
            for course in self.kurss:
                print(f"- {course}")
            else:
              print(f"Skolā {self.name} nav pievienotu kursu.")
school1 = School("RVVĢ")
school1.add_course("Python")
school1.add_course("psiholoģija")

class Grade:
    def __init__(self, student, course, grade):
        self.student = student
        self.course = course
        self.grade = grade
    def display_grade (self):
        print (f"{self.student} atzīme kursā {self.course}: {self.grade}")
grade1 = Grade("Uģis", "Matemātika", 10)
grade1.display_grade()

class Exam:
    def __init__(self, course, date):
        self.course = course
        self.date = date
    
