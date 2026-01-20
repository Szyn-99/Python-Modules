class GardenError(Exception):
    pass
class IsValidNameError(GardenError):
    pass
class WaterLevelError(GardenError):
    pass
class SunLightHoursError(GardenError):
    pass

def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int) -> str:
    try:
        if plant_name == None or plant_name == "":
            raise IsValidNameError("Error: Plant name cannot be empty!")
        elif water_level > 10:
            raise WaterLevelError(f"Error: Water level {water_level} is too high (max 10)")
        elif water_level < 1:
            raise WaterLevelError(f"Error: Water level {water_level} is too low (min 1)")
        elif sunlight_hours < 2:
            raise SunLightHoursError(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
        elif sunlight_hours > 12:
            raise SunLightHoursError(f"Error: Sunlight hours {sunlight_hours} is too high (max 12)")
        else:
            return f"Plant '{plant_name}' is healthy!"
    except GardenError as hadi9a:
        print(hadi9a)


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")
    
    print("Testing good values...")
    try:
        result = check_plant_health("tomato", 5, 8)
        if result:
            print(result)
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()
    
    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 8)
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()
    
    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 8)
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()
    
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()
    
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()