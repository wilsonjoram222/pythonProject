class ApplicationForm:

    def capture_info(self):
        print("===== SCHOOL APPLICATION FORM =====")

        self.name = input("Enter Name: ")
        self.age = input("Enter Age: ")
        self.gender = input("Enter Gender: ")

        # Course selection
        print("\nAvailable Courses")
        print("1. Software Engineering")
        print("2. Information Technology")
        print("3. Computer Science")
        print("4. Business Administration")
        print("5. Accounting")

        choice = int(input("Select Course (1-5): "))

        if choice == 1:
            self.course = "Software Engineering"
        elif choice == 2:
            self.course = "Information Technology"
        elif choice == 3:
            self.course = "Computer Science"
        elif choice == 4:
            self.course = "Business Administration"
        elif choice == 5:
            self.course = "Accounting"
        else:
            self.course = "Not Selected"

        self.phone = input("Enter Student Phone Number: ")

        print("\n----- Guardian Information -----")
        self.guardian_name = input("Guardian Name: ")
        self.relationship = input("Relationship (Father/Mother/Guardian): ")
        self.guardian_phone = input("Guardian Phone Number: ")
        self.guardian_address = input("Guardian Address: ")

    def display_info(self):
        print("\n===== APPLICATION DETAILS =====")
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Course:", self.course)
        print("Student Phone:", self.phone)

        print("\n----- Guardian Details -----")
        print("Guardian Name:", self.guardian_name)
        print("Relationship:", self.relationship)
        print("Guardian Phone:", self.guardian_phone)
        print("Guardian Address:", self.guardian_address)

        print("\nApplication Status: RECEIVED")


# Create object
student = ApplicationForm()

# Capture information
student.capture_info()

# Display information
student.display_info()