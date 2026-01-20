def check_temperature(temp_str: str) -> int | None:
    try:
        try:
            temp = int(temp_str)
        except ValueError:
            raise ValueError(f"Error: '{temp_str}' is not a valid number")
        if(temp > 40):
            raise ValueError(f"Error: {temp}°C is too hot for plants (max 40°C)")
        elif temp < 0:
            raise ValueError(f"Error: {temp}°C is too cold for plants (min 0°C)")
        else :
            print(f"Temperature {temp}°C is perfect for plants!")
    except Exception as Error:
        print(Error)
        return None

    
def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")   
    print("Testing temperature: 25")
    check_temperature("25") 
    print()
    print("Testing temperature: abc")
    check_temperature("abc")
    print()
    print("Testing temperature: 100")
    check_temperature("100")
    print()
    print("Testing temperature: -50")
    check_temperature("-50")
    print()
    print("All tests completed - program didn't crash!")
    
if __name__ == "__main__":
    test_temperature_input()