def plant_in_a_garden() -> None:
    """Defining class attributes based on instance variables"""
    name = "Rose"
    height = "25cm"
    age = "30 days"
    """here we print the plant information"""
    print(f"Plant: {name}\nHeight: {height}\nAge: {age}")


def main():
    """main function to call the method above and run the program"""
    print("=== Welcome to My Garden ===")
    plant_in_a_garden()
    print("=== End of Program ===")


if __name__ == "__main__":
    """here we use the (if __name__ == "__main__") pattern to call
    to execute the main function only when the script in the main file"""
    main()
