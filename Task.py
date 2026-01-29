# ---------- Standalone Functions ----------

def calculate_final_score(internal, external):
    if not (0 <= internal <= 40 and 0 <= external <= 60):
        raise ValueError("Invalid marks: Internal (0–40), External (0–60)")
    return internal + external


def calculate_grade(score):
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 55:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "Fail"


# ---------- Base Class ----------

class Person:
    def __init__(self, pid, name):
        self.id = pid
        self.name = name

    def get_role(self):
        return "Person"

    def display_details(self):
        print(f"ID: {self.id}, Name: {self.name}")


# ---------- Student Class ----------

class Student(Person):
    def __init__(self, pid, name, department):
        super().__init__(pid, name)
        self.department = department
        self.courses = {}  # {course_name: {"internal": x, "external": y}}

    def enroll_course(self, course_name):
        self.courses[course_name] = {"internal": None, "external": None}

    def add_marks(self, course_name, internal, external):
        if course_name not in self.courses:
            raise ValueError("Student not enrolled in this course")
        self.courses[course_name]["internal"] = internal
        self.courses[course_name]["external"] = external

    def calculate_result(self, course_name):
        marks = self.courses.get(course_name)
        if marks is None or marks["internal"] is None:
            return None
        score = calculate_final_score(marks["internal"], marks["external"])
        grade = calculate_grade(score)
        return score, grade

    def get_role(self):
        return "Student"


# ---------- Professor Class ----------

class Professor(Person):
    def __init__(self, pid, name, department, subjects_handled):
        super().__init__(pid, name)
        self.department = department
        self.subjects_handled = subjects_handled

    def assign_marks(self, student, course_name, internal, external):
        student.add_marks(course_name, internal, external)

    def get_role(self):
        return "Professor"

    def display_details(self):
        print(
            f"ID: {self.id}, Name: {self.name}, "
            f"Subjects: {', '.join(self.subjects_handled)}"
        )


# ---------- Course Class ----------

class Course:
    def __init__(self, course_name, professor):
        self.course_name = course_name
        self.professor = professor
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        student.enroll_course(self.course_name)

    def show_course_report(self):
        print(f"\nCourse Report: {self.course_name}")
        for student in self.students:
            result = student.calculate_result(self.course_name)
            if result:
                score, grade = result
                print(f"{student.name} → Score: {score}, Grade: {grade}")
            else:
                print(f"{student.name} → Marks not assigned")


# ---------- Object Creation & Flow ----------

# 1. Create Professor
professor1 = Professor(
    pid=101,
    name="Dr. Rao",
    department="Computer Science",
    subjects_handled=["Python Programming"]
)

# 2. Create Students
student1 = Student(201, "Mohana", "Computer Science")
student2 = Student(202, "Ananya", "Computer Science")

# 3. Create Course
course1 = Course("Python Programming", professor1)

# 4. Enroll Students
course1.add_student(student1)
course1.add_student(student2)

# 5. Professor assigns marks
professor1.assign_marks(student1, "Python Programming", 35, 50)
professor1.assign_marks(student2, "Python Programming", 28, 42)

# 6. Individual Student Results
print("\nIndividual Student Results:")
for student in [student1, student2]:
    score, grade = student.calculate_result("Python Programming")
    print(f"{student.name} → Score: {score}, Grade: {grade}")

# 7. Full Course Report
course1.show_course_report()

# 8. Polymorphism Demonstration
print("\nPolymorphism Output:")
people = [student1, professor1]
for person in people:
    print(f"Role: {person.get_role()}")
    person.display_details()