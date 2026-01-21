class GardenError(Exception):
    pass


class IsValidNameError(GardenError):
    pass


class WaterLevelError(GardenError):
    pass


class SunLightHoursError(GardenError):
    pass

class Plant:
    def __init__(self, plant_name: str, water_level: int, sunlight_hours: int):
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

if __name__ == "__main__":
    try:
        rose = Plant("Rose", 5, 6)
        maroc = Plant("Maroc", 3, 18)
    except GardenError as garden_err:
        print(garden_err)
    print(rose)