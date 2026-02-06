def garden_operations(
    division: int = None, file: str = None, value: str = None, key: str = None
) -> None:
    if division is not None:
        division / 0
    elif file is not None:
        open(file, "r")
    elif value is not None:
        int(value)
    elif key is not None:
        larousse = {}
        larousse[key]
    else:
        print("No operation specified")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    print("Testing ValueError...")
    try:
        garden_operations(value="abc", a=open("f"))
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    except Exception as e:
        print(f"Caught unexpected error: {e}")

    print()

    print("Testing ZeroDivisionError...")
    try:
        garden_operations(division=5)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except Exception as e:
        print(f"Caught unexpected error: {e}")
    print()

    print("Testing FileNotFoundError...")
    try:
        garden_operations(file="alo.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'alo.txt'")
    except Exception as e:
        print(f"Caught unexpected error: {e}")
    print()

    print("Testing KeyError...")
    try:
        garden_operations(key="alo_plant")
    except KeyError:
        print("Caught KeyError: 'alo_plant'")
    except Exception as e:
        print(f"Caught unexpected error: {e}")
    print()

    print("Testing multiple errors together...")
    try:
        garden_operations(value="xyz", division=3, file="alo.txt")
    except (ValueError, ZeroDivisionError,
            FileNotFoundError, KeyError) as lereur:
        print(f"Caught {lereur.__class__.__name__}: {lereur}")
        print("Caught an error, but program continues!")
    except Exception as e:
        print(f"Caught unexpected error: {e}")
    print()
    print("All error types tested successfully")


if __name__ == "__main__":
    test_error_types()
