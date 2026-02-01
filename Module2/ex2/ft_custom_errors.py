class GardenError(Exception):
    def __init__(self, message: str = "GardenError") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "PlantError") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "WaterError") -> None:
        super().__init__(message)


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
    except Exception as e:
        print(f"Caught unexpected exception: {e}")
    print()
    print("Testing WaterError...")
    try:
        water_plant(0)
    except WaterError as e:
        print(e)
    except Exception as e:
        print(f"Caught unexpected exception: {e}")
    print()
    print("Testing catching all garden errors...")
    try:
        water_plant(0)
    except GardenError as e:
        print(e)
    except Exception as e:
        print(f"Caught unexpected exception: {e}")
    try:
        plant_status("wilting")
    except GardenError as e:
        print(e)
    except Exception as e:
        print(f"Caught unexpected exception: {e}")
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
