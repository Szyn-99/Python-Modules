def garden_operations(op: int, division: int=None, file: str=None, value: str=None, key: str=None) -> None:
    try:
        if(op == 1):
            try:
                a = 1 / 0
            except ZeroDivisionError:
                raise ZeroDivisionError("Caught ZeroDivisionError: division by zero")
        elif(op == 2):
            try:
                stream = open(file, "r")
            except FileNotFoundError:
                raise FileNotFoundError(f"Caught FileNotFoundError: No such file '{file}'")
        elif(op == 3):
            try:
                another_a = int(value)
            except ValueError:
                raise ValueError("Caught ValueError: invalid literal for int()")
        elif(op == 4):
            try:
                dictionary = {}
                keyv = dictionary[key]
            except KeyError:
                raise KeyError(f"Caught KeyError: '{key}'")
        else:
            print("No Operation Specified")
            return None
    except Exception as a:
        print(a)
        return None




def test_garden_operations() -> None:
    print("=== Garden Error Types Demo ===")
    
    print("Testing ValueError...")
    garden_operations(op=3, value="abc")
    print()
    print("Testing ZeroDivisionError...")
    garden_operations(op=1)
    print()
    
    print("Testing FileNotFoundError...")
    garden_operations(op=2, file="missing.txt")
    print()
    
    print("Testing KeyError...")
    garden_operations(op=4, key="missing_plant")
    print()
    
    # print("Testing multiple errors together...")

    # garden_operations(op=3, value="xyz")

    # print("Caught an error, but program continues!")
    
    print("All error types tested successfully")


if __name__ == "__main__":
    test_garden_operations()
