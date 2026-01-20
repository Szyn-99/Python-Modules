def garden_operations(
    division: int = None, file: str = None, value: str = None, key: str = None
) -> None:
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
    try:
        garden_operations(value="abc")
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")

    print()

    print("Testing ZeroDivisionError...")
    try:
        garden_operations(division=5)
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")

    print()

    print("Testing FileNotFoundError...")
    try:
        garden_operations(file="alo.txt")
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()

    print("Testing KeyError...")
    try:
        garden_operations(key="alo_plant")
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()

    print("Testing multiple errors together...")
    try:
        garden_operations(value="xyz", division=3, file="alo.txt")
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()
    print("Caught an error, but program continues!")
    print()
    print("All error types tested successfully")


if __name__ == "__main__":
    test_garden_operations()
