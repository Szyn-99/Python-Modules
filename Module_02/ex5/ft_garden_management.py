class GardenError(Exception):
    pass


class IsValidNameError(GardenError):
    pass


class WaterLevelError(GardenError):
    pass


class SunLightHoursError(GardenError):
    pass


class Plant:
    def __init__(self, plant_name: str, water_level:
                 int, sunlight_hours: int) -> None:
        if plant_name is None or plant_name == "":
            raise IsValidNameError("Plant name cannot be empty!")
        elif water_level > 10:
            raise WaterLevelError(
                f"Water level {water_level} is too high (max 10)")
        elif water_level < 1:
            raise WaterLevelError(
                f"Water level {water_level} is too low (min 1)")
        elif sunlight_hours < 2:
            raise SunLightHoursError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)"
            )
        elif sunlight_hours > 12:
            raise SunLightHoursError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)"
            )
        else:
            self.plant_name = plant_name
            self.water_level = water_level
            self.sunlight_hours = sunlight_hours


class GardenManager:

    def __init__(self, water_total: int) -> None:
        self.garden = []
        self.adding_flag = 1
        self.water_flag = 1
        self.health_flag = 1
        self.water_total = water_total

    def add_plant(self, plant_name: str,
                  water_level: int, sunlight_hours: int) -> None:
        try:
            if self.adding_flag == 1:
                self.adding_flag = 0
                print("Adding plants to garden...")
            plant = Plant(plant_name, water_level, sunlight_hours)
            self.garden += [plant]
            print(f"Added {plant_name} successfully")
        except GardenError as error_add:
            print(f"Error adding plant: {error_add}")

    def water_plant(self, water_to_water: int) -> None:
        try:
            print("Watering plants...")
            print("Opening watering system")
            for plant in self.garden:
                if self.water_total < water_to_water:
                    raise WaterLevelError("Not enough water in tank")
                self.water_total -= water_to_water
                plant.water_level += water_to_water
                print(f"Watering {plant.plant_name} - success")
        except GardenError as ga:
            print(f"Caught GardenError: {ga}")
            print("System recovered and continuing...")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant: Plant) -> str:
        try:
            if self.health_flag == 1:
                self.health_flag = 0
                print("Checking plant health...")
            if plant.water_level > 10:
                raise WaterLevelError(
                    f"Water level {plant.water_level} is too high (max 10)"
                )
            elif plant.water_level < 1:
                raise WaterLevelError(
                    f"Water level {plant.water_level} is too low (min 1)"
                )
            elif plant.sunlight_hours < 2:
                raise SunLightHoursError(
                    f"Sunlight hours {plant.sunlight_hours} is too low (min 2)"
                )
            elif plant.sunlight_hours > 12:
                raise SunLightHoursError(
                    f"Sunlight hours {plant.sunlight_hours} is too high "
                    f"(max 12)"
                )
            else:
                return (f"{plant.plant_name}: healthy (water: "
                        f"{plant.water_level}, sun: {plant.sunlight_hours})")
        except GardenError as error:
            return f"Error checking {plant.plant_name}: {error}"


def test_garden_management():
    print("=== Garden Management System ===")

    garden = GardenManager(10)
    try:
        garden.add_plant("tomato", 5, 8)
        garden.add_plant("batata", 5, 8)
        garden.add_plant("lettuce", 8, 8)
        garden.add_plant("", 4, 4)
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()

    try:
        garden.water_plant(4)
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()

    try:
        for plant in garden.garden:
            print(garden.check_plant_health(plant))
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()

    print("Testing error recovery...")
    try:
        garden.water_plant(50)
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
