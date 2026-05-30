class farmer:
    def __init__(self, name="", quality="", weight="", crop_type="", address=""):
        self.name = name
        self.quality = quality
        self.weight = weight
        self.crop_type = crop_type
        self.address = address

    def capture_information(self):
        self.name = input("Enter your product name: ")
        self.quality = input("Enter your product quality: ")
        self.weight = int(input("Enter your product quantity: "))
        self.address = input("Enter your address: ")
        self.crop_type = input("Enter your crop type: ")


    def display_information(self):
        print(self.name)
        print(self.quality)
        print(self.weight)
        print(self.crop_type)
        print(self.address)


farmer_1 = farmer()
farmer_1.capture_information()
farmer_1.display_information()
