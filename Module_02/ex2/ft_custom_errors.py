class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def water_plant(tank: int) -> None:
    if tank <= 0:
        raise WaterError(
            "Caught WaterError: Not enough water in the tank!")
    else:
        print("Plants are fine !")


def plant_status(plant_status: str) -> None:
    if plant_status == "wilting":
        raise PlantError("Caught PlantError: The tomato plant is wilting!")
    else:
        print("Plants are fine !")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        plant_status("wilting")
    except PlantError as e:
        print(e)
    print()
    print("Testing WaterError...")
    try:
        water_plant(0)
    except WaterError as e:
        print(e)
    print()
    print("Testing catching all garden errors...")
    try:
        water_plant(0)
    except GardenError as e:
        print(e)
    try:
        plant_status("wilting")
    except GardenError as e:
        print(e)
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
