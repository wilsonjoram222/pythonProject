class ApplicationForm:

    def capture_info(self):
        print("\n===== SCHOOL APPLICATION FORM =====")
        print("===== UICT DEPARTMENT OF INFORMATION TECHNOLOGY =====")

        self.name = input("Enter Name: ")
        self.age = input("Enter Age: ")
        self.gender = input("Enter Gender: ")
        self.date_of_birth = input("Enter Date of Birth: ")
        self.nationality = input("Enter Nationality: ")
        self.home_district = input("Enter Home District: ")
        self.religion = input("Enter Religion: ")

        # Course selection
        print("\nAvailable Courses")
        print("1. Software Engineering")
        print("2. Information Technology")
        print("3. Computer Science")
        print("4. Business Administration")
        print("5. Accounting")

        choice = int(input("Select Course (1-5): "))

        courses = {
            1: "Software Engineering",
            2: "Information Technology",
            3: "Computer Science",
            4: "Business Administration",
            5: "Accounting"
        }

        self.course = courses.get(choice, "Not Selected")

        self.phone = input("Enter Student Phone Number: ")
        self.email = input("Enter Student Email: ")

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
        print("Date of Birth:", self.date_of_birth)
        print("Nationality:", self.nationality)
        print("Home District:", self.home_district)
        print("Religion:", self.religion)
        print("Course:", self.course)
        print("Student Phone:", self.phone)
        print("Student Email:", self.email)

        print("\n----- Guardian Details -----")
        print("Guardian Name:", self.guardian_name)
        print("Relationship:", self.relationship)
        print("Guardian Phone:", self.guardian_phone)
        print("Guardian Address:", self.guardian_address)

        print("\nApplication Status: RECEIVED")

    def start(self):
        self.capture_info()
        self.display_info()

        again = input("\nDo you want to enter another application? (yes/no): ").lower()

        if again == "yes":
            print("\nStarting another application...\n")
            self.start()      # this makes the form Recursive
        else:
            print("\nThank you for using the application system.")


# Create object
student = ApplicationForm()

# Start the recursive application
student.start()