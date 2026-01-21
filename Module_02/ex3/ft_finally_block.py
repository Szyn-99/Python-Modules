class InvalidPlantError(Exception):
    pass


def water_plants(plant_list: list):
    print("Opening watering system")
    try:
        for each in plant_list:
            if each is None or each == "None":
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
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()

    print("Testing with error...")
    try:
        water_plants(["tomato", None])
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
