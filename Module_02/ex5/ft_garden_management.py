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
    
    def water_plant() -> None:
        if GardenManager.water == 1:
            GardenManager.water = 0
            print("Opening watering system")
            print("Watering plants...")
        for plant in GardenManager.garden:
            plant.water_level += 1
            print(f"Watering {plant.plant_name} - success")
            
    water_plant = staticmethod(water_plant)
    
    
    
    
    
    
    
    
    
    
    @staticmethod
    def show_plant():
        for plant in GardenManager.garden:
            print(plant.plant_name, plant.water_level, plant.sunlight_hours)
   



def test():
    garden = GardenManager()
    garden.add_plant("khizo", 4, 4)
    garden.add_plant("btata", 4, 4)
    garden.add_plant("", 4, 4)
    garde.water_plant
    garden.show_plant()
    print()
    
    
test()