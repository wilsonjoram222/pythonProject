class ClientsFormRegistration():
    #cleints info
    print("website desgining cleints form by kawuma joram 2025/dswe/eve/0590")
    def capture_information(self):
        self.client_name = input("Please enter your client name: ")
        self.client_email = input("Please enter your client email: ")
        self.client_address = input("Please enter your client address: ")
        self.client_phone = input("Please enter your client phone: ")

       #busines type
        self.business_type = input("Please enter your business type: ")
        self.business_name = input("Please enter your business name: ")
        self.business_address = input("Please enter your business address: ")
        self.business_description = input("Please enter your business description: ")

         #website details
        print("\nWebsite Type")
        print("1. Business Website")
        print("2. E-Commerce Website")
        print("3. Portfolio Website")
        print("4. School Website")
        print("5. NGO Website")
        print("6. Blog")
        print("7. Personal Website")
        print("8. Other")
        choice = int(input("Choose Website Type (1-7): "))

        website_types = {
            1: "Business Website",
            2: "E-Commerce Website",
            3: "Portfolio Website",
            4: "School Website",
            5: "NGO Website",
            6: "Blog",
            7: "Personal Website",
            8: "Other"
        }

        self.website_type = website_types.get(choice, "Custom Website")

        self.website_domain = input("Preferred Domain Name (e.g., mycompany.com): ")
        self.has_domain = input("Does your website domain exist? (Y/N): ")
        self.has_hosting = input("Does your website hosting exist? (Y/N): ")
        #Design preference
        self.secondary_color = input("Please enter your secondary color: ")
        self.primary_color = input("Please enter your primary color: ")
        self.favourite_website = input("Please enter your favourite website for reference: ")
      #features required
        self.contact_form =input("Do you want contact form? (Y/N): ")
        self.gallarey = input("Do you want Gallarey? (Y/N): ")
        self.online_payment = input("Do you want online payment? (Y/N): ")
        self.blog_post = input("Do you want Blog post? (Y/N): ")
        self.social_media = input("Do you want social media? (Y/N): ")
        self.google_map = input("Do you want Google Map? (Y/N): ")
        #content
        self.has_logo = input("Do you have a logo for your website? (Y/N): ")
        self.has_images = input("Do you have images images for your website? (Y/N): ")
        self.has_content = input("Do you have written  content? (Y/N): ")
        #project details
        self.deadline = input("Please enter your deadline: ")
        self.start_date = input("Please enter your start date: ")
        self.estimated_budget = input("Please enter your estimated budget: ")

        self.additional_information = input("Please enter your additional requirements: ")

        #display info
    def display_information(self):
        print("\nclients information")
        print("-------------------------------------")
        print(" Client Name", self.client_name)
        print(" Client Email", self.client_email)
        print(" Client Address", self.client_address)
        print(" Client Phone", self.client_phone)
            #business info
        print("\nbusiness information")
        print("---------------------------------------")
        print(" Business Type", self.business_type)
        print(" Business Name", self.business_name)
        print(" Business Address", self.business_address)
        print(" Business Description", self.business_description)
        print("\nwebsite details")
        print("--------------------------------")
        print(" Website Type", self.website_type)
        print(" Preferred Domain", self.website_domain)
        print(" Has Domain", self.has_domain)
        print(" Has Hosting", self.has_hosting)

        print("\ndesign preference")
        print("------------------------")
        print("primary color", self.primary_color)
        print("secondary color", self.secondary_color)
        print("Reference website", self.favourite_website)

        print("\nfeatures requested")
        print("------------------")
        print("googlemap", self.google_map)
        print("contact form", self.contact_form)
        print("gallarey", self.gallarey)
        print("online payment", self.online_payment)
        print("blog post", self.blog_post)
        print("social media", self.social_media)

        print("\ncontent provided")
        print("-----------------")
        print("logo", self.has_logo)
        print("images", self.has_images)
        print("content", self.has_content)


        print("\nproject information")
        print("-----------------")
        print("deadline", self.deadline)
        print("start date", self.start_date)
        print("estimated budget", self.estimated_budget)
        print("additional information", self.additional_information)

        print("Project Status: Received Successfully")
#main information
cleint = ClientsFormRegistration()
cleint.capture_information()
cleint.display_information()








