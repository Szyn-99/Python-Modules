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
    except WaterError as water_err:
        print(water_err)


def plant_status(plant_status: str) -> None:
    try:
        if plant_status == "wilting":
            raise PlantError("Caught PlantError: The tomato plant is wilting!")
    except PlantError as plant_err:
        print(plant_err)


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    plant_status("wilting")
    print()
    print("Testing WaterError...")
    water_plant(0)
    print()
    print("Testing catching all garden errors...")
    try:
        water_plant(0, "")
        plant_status("wilting")
    except Exception as e:
        print(e)
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
