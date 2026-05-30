
class Course:
    def __init__(self, course_name, course_code, credit_unit):
        self.course_name = course_name
        self.course_code = course_code
        self.credit_unit = credit_unit
        self.lecturer = None
        self.student_enrolled = 0

    def assign\_lecturer\(self, lecturer\_name\):
        self.lecturer = lecturer\_name

    def enroll\_student\(self, number\):
        self.student\_enrolled += number

    def display\_info\(self\):
        print\(""\)
        print\("Course Code:", self.course\_code\)
        print\("Course Name:", self.course\_name\)
        print\("Credit Units:", self.credit\_unit\)
        print\("Lecturer:", self.lecturer\)
        print\("Students Enrolled:", self.student\_enrolled\)

course_1 = Course("Diploma in Software Engineering", "SWE1101", 5)
course_1.assign_lecturer("Okeny Lumbert")
course_1.enroll_student(1)
course_1.display_info()
Department
----------------------------------------------------------

class Department:
    def __init__(self, department_ID, department_name, head_of_department):
        self.department_ID = department_ID
        self.department_name = department_name
        self.head_of_department = head_of_department
        self.courses = []
        self.staff_members = []

    def add\_course\(self, course\):
        self.courses.append\(course\)

    def add\_staff\(self, staff\):
        self.staff\_members.append\(staff\)

    def display\_department\(self\):
        print\(""\)
        print\("Department ID:", self.department\_ID\)
        print\("Department Name:", self.department\_name\)
        print\("Head of Department:", self.head\_of\_department\)

        for course in self.courses:
            print\("Course -", course\)

        for staff in self.staff\_members:
            print\("Staff Member -", staff\)

department_1 = Department(1, "ICT depertment", "Enkuru James")
department_1.add_course("Computer Science")
department_1.add_staff("Okello Joker")
department_1.display_department()

department_1 = Department(2, "Business department", "Okurut Derrick")
department_1.add_course("Business Computing")
department_1.add_staff("Ojera Kenneth")
department_1.display_department()

#Staff Class
------------------------------------------------------------------------

class Staff:
    def __init__(self, staff_id, staff_name, position, salary):
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.position = position
        self.salary = salary
        self.department = None

    def assign\_department\(self, department\_name\):
        self.department = department\_name

    def increase\_salary\(self, amount\):
        self.salary = amount
        # self.salary += amount

    def display\_staff\_info\(self\):
        print\(""\)
        print\("Staff ID:", self.staff\_id\)
        print\("Name:", self.staff\_name\)
        print\("Position:", self.position\)
        print\("Salary:", self.salary\)
        print\("Department:", self.department\)

staff_1 = Staff(1, "OKOT EMMANUEL", "LECTURER", 500000)
staff_1.assign_department(department_name="ICT department")
staff_1.increase_salary(500000)
staff_1.display_staff_info()

staff_1 = Staff(2, "AYELLA DANIEL", "LECTURER", 500000)
staff_1.assign_department(department_name="ICT department")
staff_1.increase_salary(500000)
staff_1.display_staff_info()