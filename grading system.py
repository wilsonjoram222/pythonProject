class GradingSystem:

    def capture_marks(self):
        print("===== UICT GRADING SYSTEM =====")

        self.name = input("Enter Student Name: ")
        self.reg_no = input("Enter Registration Number: ")
        self.course = input("Enter Course: ")

        # Marks
        self.coursework = float(input("Enter Coursework Marks (Out of 40): "))
        self.final_exam = float(input("Enter Final Exam Marks (Out of 60): "))

        # Calculate Total
        self.total = self.coursework + self.final_exam

        # Determine Grade
        if self.total >= 80:
            self.grade = "A"
            self.remark = "Excellent"

        elif self.total >= 70:
            self.grade = "B"
            self.remark = "Very Good"

        elif self.total >= 60:
            self.grade = "C"
            self.remark = "Good"

        elif self.total >= 50:
            self.grade = "D"
            self.remark = "Pass"

        else:
            self.grade = "F"
            self.remark = "Fail"

    def display_result(self):
        print("\n===== STUDENT RESULT =====")
        print("Student Name:", self.name)
        print("Registration Number:", self.reg_no)
        print("Course:", self.course)
        print("Coursework Marks:", self.coursework, "/40")
        print("Final Exam Marks:", self.final_exam, "/60")
        print("Total Marks:", self.total, "/100")
        print("Grade:", self.grade)
        print("Remark:", self.remark)

    def start(self):
        self.capture_marks()
        self.display_result()

        choice = input("\nDo you want to grade another student? (yes/no): ").lower()

        if choice == "yes":
            self.start()
        else:
            print("\nThank you for using the Grading System.")


# Create Object
student = GradingSystem()

# Start Program
student.start()