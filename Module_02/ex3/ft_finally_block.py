class InvalidPlantError(Exception):
    def __init__(self, message: str = "InvalidPlantError") -> None:
        super().__init__(message)


def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for each in plant_list:
            if each is None or each == "":
                raise InvalidPlantError(
                    f"Error: Cannot water {each} - invalid plant!")
            print(f"Watering {each}")
        print("Watering completed successfully!")
    except InvalidPlantError as plant:
        print(plant)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    print("Testing normal watering...")
    try:
        water_plants(["tomato", "lettuce", "carrots"])
    except Exception as error:
        print(f"Subject Requirement: {error}")
    finally:
        print("Cleanup after normal watering")
    print()

    print("Testing with error...")
    try:
        water_plants(["tomato", None])
    except Exception as error:
        print(f"Subject Requirement: {error}")
    print()

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
