# List to store products
products = []

# function to handle the "cancel" input
def check_for_cancel(input_value):
    if (input_value == "cancel"):
        print("Operation cancelled.")
        return True
    return False


# Display menu options
def show_menu():
    print("Menu")
    print("1. Show all products")
    print("2. Add new product")
    print("3. Delete a product")
    print("4. Update a product")
    print("5. Exit")


# Function to check if products are available
def is_products_available():
    if (len(products) == 0):
        print("No products available.")
        return False
    return True


# Function to show all products in a tabular format using f-strings
def show_all_products():
    if (not is_products_available()):
        return

    # Manually adding spaces to align the headers
    print(
        f"{'PID':10} {'Name':20} {'Description':30} {'Rating':10} {'Price':10} {'Image':30}"
    )
    print("-" * 100)

    # Print each product in a row
    for product in products:
        print(
            f"{product['pid']:10} {product['name']:20} {product['description']:30} {str(product['rating']):10} {str(product['price']):10} {product['image']:30}"
        )


# Function to add a new product using a dictionary for input
def add_product():
    print("Enter product details:")

    # Taking input and storing directly into a dictionary
    product = {
        "pid": input("Product ID: "),
        "name": input("Product Name: "),
        "description": input("Product Description: "),
        "rating": float(input("Product Rating: ")),
        "price": int(input("Product Price: ")),
        "image": input("Product Image URL: "),
    }

    # Adding product to the list
    products.append(product)
    print("Product added successfully!")


# Function to delete a product
def delete_product():
    if (not is_products_available()):
        return

    while (True):
        pid_to_delete = input("Enter Product ID to delete or type 'cancel' to abort: ")

        # Check if the user wants to cancel the operation
        if (check_for_cancel(pid_to_delete)):
            break

        # Find the product by PID
        for product in products:
            if (product["pid"] == pid_to_delete):
                products.remove(product)
                print(f"Product with ID {pid_to_delete} deleted successfully!")
                return

        # If PID not found
        print(
            f"No product found with ID {pid_to_delete}. Please try again or type 'cancel' to exit."
        )


# Function to update a product
def update_product():
    if (not is_products_available()):
        return

    while (True):
        pid_to_update = input("Enter Product ID to update or type 'cancel' to abort: ")

        # Check if the user wants to cancel the operation
        if (check_for_cancel(pid_to_update)):
            break

        # Find the product by PID
        for product in products:
            if (product["pid"] == pid_to_update):
                # Display current product details
                print(f"Current Name: {product['name']}")
                print(f"Current Description: {product['description']}")
                print(f"Current Rating: {product['rating']}")
                print(f"Current Price: {product['price']}")
                print(f"Current Image URL: {product['image']}")

                # Keep prompting the user until they enter a valid field
                while (True):
                    # Ask user what to update
                    field_to_update = input(
                        "What would you like to update (name, description, rating, price, image)? "
                    )

                    if (field_to_update == "name"):
                        new_name = input("Enter new Name: ")
                        product["name"] = new_name
                        print("Product name updated successfully!")
                        return
                    elif (field_to_update == "description"):
                        new_description = input("Enter new Description: ")
                        product["description"] = new_description
                        print("Product description updated successfully!")
                        return
                    elif (field_to_update == "rating"):
                        new_rating = input("Enter new Rating: ")
                        product["rating"] = new_rating
                        print("Product rating updated successfully!")
                        return
                    elif (field_to_update == "price"):
                        new_price = int(input("Enter new Price: "))
                        product["price"] = new_price
                        print("Product price updated successfully!")
                        return
                    elif (field_to_update == "image"):
                        new_image = input("Enter new Image URL: ")
                        product["image"] = new_image
                        print("Product image updated successfully!")
                        return
                    else:
                        print(
                            "Invalid field. Please choose 'name', 'description', 'rating', 'price', or 'image'."
                        )
                return

        # If PID not found
        print(
            f"No product found with ID {pid_to_update}. Please try again or type 'cancel' to exit."
        )


# Main function to run the menu and handle user choices
def main():
    while (True):
        show_menu()
        user_input = input("Enter Option to Continue: ")

        if (user_input == "1"):
            show_all_products()
        elif (user_input == "2"):
            add_product()
        elif (user_input == "3"):
            delete_product()
        elif (user_input == "4"):
            update_product()
        elif (user_input == "5"):
            print("Exiting program...")
            break
        else:
            print("Invalid input, please try again.")


# Run the program
main()