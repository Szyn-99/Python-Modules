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
                f"Water level {water_level} is too high (max 10)"
            )
        elif water_level < 1:
            raise WaterLevelError(
                f"Water level {water_level} is too low (min 1)"
            )
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
    garden = []
    adding_flag = 1
    water_flag = 1
    adding_flag = 1
    water_total = 0
    def __init__(self, water_total: int) -> None:
        
        GardenManager.water_total = water_total
    
    def add_plant(plant_name: str, water_level: int, sunlight_hours: int) -> None:
        
        try:
            if GardenManager.adding_flag == 1:
                GardenManager.adding_flag = 0
                print("Adding plants to garden...")
            plant = Plant(plant_name, water_level, sunlight_hours)
            GardenManager.garden += [plant]
            print(f"Added {plant_name} successfully")
        except GardenError as error_add:
            print(f"Error adding plant: {error_add}!")
            
    add_plant = staticmethod(add_plant)
    
    def water_plant(water_to_water) -> None:
        if GardenManager.water_flag == 1:
            GardenManager.water_flag = 0
            print("Watering plants...")
            print("Opening watering system")
        try:
            for plant in GardenManager.garden:
                if GardenManager.water_total < water_to_water:
                    raise GardenError("Not enough water in tank")
                GardenManager.water_total -= water_to_water
                plant.water_level += water_to_water
                print(f"Watering {plant.plant_name} - success")
        except GardenError as ga:
            print(f"Caught GardenError: {ga}")
            print("System recovered and continuing...")
        finally:
            print("Closing watering system (cleanup)")
            
            
    water_plant = staticmethod(water_plant)
    
    
    def check_plant_health(plant: Plant) -> str:
        try:
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
                    f"Sunlight hours {plant.sunlight_hours} is too high (max 12)"
                )
            else:
                return f"{plant.plant_name}: healthy (water: {plant.water_level}, sun: {plant.sunlight_hours})"
        except GardenError as error:
            print(error)
            return None

    check_plant_health = staticmethod(check_plant_health)

def test_garden_management():
    print("=== Garden Management System ===")
    
    garden = GardenManager(100)
    try:
        garden.add_plant("tomato", 3, 8)
        garden.add_plant("lettuce", 3, 8)
        garden.add_plant("", 4, 4)
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()
    
    try:
        garden.water_plant(2)
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()
    
    print("Checking plant health...")
    try:
        for plant in GardenManager.garden:
            result = GardenManager.check_plant_health(plant)
            if result:
                print(result)
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()
    
    print("Testing error recovery...")
    GardenManager.water_flag = 1
    GardenManager.garden = []
    GardenManager.adding_flag = 1
    
    garden2 = GardenManager(5)
    try:
        garden2.add_plant("carrot", 3, 6)
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    
    try:
        garden2.water_plant(10)
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()
    
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()