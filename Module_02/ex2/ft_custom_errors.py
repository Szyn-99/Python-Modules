class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def water_plant(tank: int) -> None:
    try:
        if tank <= 0:
            raise WaterError("Caught WaterError: Not enough water in the tank!")
        else:
            print("Plants are fine !")

    except WaterError as water_err:
        print(water_err)


def plant_status(plant_status: str) -> None:
    try:
        if plant_status == "wilting":
            raise PlantError("Caught PlantError: The tomato plant is wilting!")
        else:
            print("Plants are fine !")
    except PlantError as plant_err:
        print(plant_err)


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        plant_status("wilting")
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()
    print("Testing WaterError...")
    try:
        water_plant(0)
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()
    print("Testing catching all garden errors...")
    try:
        water_plant(0)
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    try:
        plant_status("wilting")
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
