class WebsiteDesigner:

    def __init__(self, name, phone, email, client, project, budget):
        self.name = name
        self.phone = phone
        self.email = email
        self.client = client
        self.project = project
        self.budget = budget

    def display_info(self):
        print("\n" + "=" * 40)
        print("WEBSITE DESIGN PROJECT DETAILS")
        print("=" * 40)
        print("Designer Name :", self.name)
        print("Phone Number  :", self.phone)
        print("Email Address :", self.email)
        print("Client Name   :", self.client)
        print("Project Name  :", self.project)
        print("Project Budget:", self.budget)
        print("=" * 40)


def main():
    print("WEBSITE DESIGNER INFORMATION SYSTEM")

    # Capture information
    name = input("Enter Designer Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")
    client = input("Enter Client Name: ")
    project = input("Enter Project Name: ")
    budget = input("Enter Project Budget: ")

    # Create object
    designer = WebsiteDesigner(
        name,
        phone,
        email,
        client,
        project,
        budget
    )

    # Display information
    designer.display_info()


main()