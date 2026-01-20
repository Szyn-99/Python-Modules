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
            raise IsValidNameError("Error: Plant name cannot be empty!")
        elif water_level > 10:
            raise WaterLevelError(
                f"Error: Water level {water_level} is too high (max 10)"
            )
        elif water_level < 1:
            raise WaterLevelError(
                f"Error: Water level {water_level} is too low (min 1)"
            )
        elif sunlight_hours < 2:
            raise SunLightHoursError(
                f"Error: Sunlight hours {sunlight_hours} is too low (min 2)"
            )
        elif sunlight_hours > 12:
            raise SunLightHoursError(
                f"Error: Sunlight hours {sunlight_hours} is too high (max 12)"
            )
        else:
            self.plant_name = plant_name
            self.water_level = water_level
            self.sunlight_hours = sunlight_hours

        
        
        

class GardenManager:
    garden = []
    @staticmethod
    def add_plant(plant_name: str, water_level: int, sunlight_hours: int) -> None:
     try:
        plant = Plant(plant_name, water_level, sunlight_hours)
        GardenManager.garden += [plant]
     except GardenError as e:
        print(e)
    @staticmethod
    def show_plant():
        for plant in GardenManager.garden:
            print(plant.plant_name)
    def check_plant_health(plant: Plant) -> str:
        try:
            if plant_name is None or plant_name == "":
                raise IsValidNameError("Error: Plant name cannot be empty!")
            elif water_level > 10:
                raise WaterLevelError(
                    f"Error: Water level {water_level} is too high (max 10)"
                )
            elif water_level < 1:
                raise WaterLevelError(
                    f"Error: Water level {water_level} is too low (min 1)"
                )
            elif sunlight_hours < 2:
                raise SunLightHoursError(
                    f"Error: Sunlight hours {sunlight_hours} is too low (min 2)"
                )
            elif sunlight_hours > 12:
                raise SunLightHoursError(
                    f"Error: Sunlight hours {sunlight_hours} is too high (max 12)"
                )
            else:
                return f"Plant '{plant_name}' is healthy!"
        except GardenError as hadi9a:
            print(hadi9a)



def test():
    garden = GardenManager()
    garden.add_plant("test", 0, 4)
    garden.show_plant()
    print()
    
    
test()