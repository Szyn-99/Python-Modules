def garden_operations(division: int = None, file: str = None, value: str = None, key: str = None) -> None:
    try:
        if division != None:
            a = division / 0
        elif file != None:
            stream = open(file, "r")
        elif value != None:
            another_a = int(value)
        elif key != None:
            larousse = {}
            keyv = larousse[key]
        else:
            print("No operation specified")
            return None

    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    except KeyError:
        print(f"Caught KeyError: '{key}'")

    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{file}'")

    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")




def test_garden_operations() -> None:
    print("=== Garden Error Types Demo ===")
    
    print("Testing ValueError...")
    garden_operations(value="abc")
    
    print()
    
    print("Testing ZeroDivisionError...")
    garden_operations(division=5)

    print()
    
    print("Testing FileNotFoundError...")
    garden_operations(file="alo.txt")
    print()
    
    print("Testing KeyError...")
    garden_operations(key="alo_plant")
    print()
    
    print("Testing multiple errors together...")
    garden_operations(value="xyz", division=3, file="alo.txt")
    print()
    print("Caught an error, but program continues!")
    print()
    print("All error types tested successfully")


if __name__ == "__main__":
    test_garden_operations()
