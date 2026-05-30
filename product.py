class Product:
    def __init__(self, product_name="", product_price="", product_quantity="",
                 product_description="", product_image="", product_size=""):
        self.product_name = product_name
        self.product_price = product_price
        self.product_quantity = product_quantity
        self.product_description = product_description
        self.product_image = product_image
        self.product_size = product_size

    def capture_information(self):
        self.product_name = input("Enter your product name: ")
        self.product_price = input("Enter your product price: ")
        self.product_quantity = input("Enter your product quantity: ")
        self.product_description = input("Enter your product description: ")
        self.product_image = input("Enter your product image: ")
        self.product_size = input("Enter your product size: ")

    def display_information(self):
        print("\n--- Product Information ---")
        print("Product name:", self.product_name)
        print("Product price:", self.product_price)
        print("Product quantity:", self.product_quantity)
        print("Product description:", self.product_description)
        print("Product image:", self.product_image)
        print("Product size:", self.product_size)


# First product
product_1 = Product()
product_1.capture_information()
product_1.display_information()

# Second product
product_2 = Product()
product_2.capture_information()
product_2.display_information()