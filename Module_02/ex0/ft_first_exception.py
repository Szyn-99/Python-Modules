def check_temperature(temp_str: str) -> int | None:
    try:
        temp = int(temp_str)
    except ValueError:
        return print(f"Error: '{temp_str}' is not a valid number")
    except Exception as hh:
        return print(f"Something went wrong {hh}")
    if(temp > 40):
        raise ValueError(f"Error: {temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        return print(f"Error: {temp}°C is too cold for plants (min 0°C)")
    else :
        return print(f"Temperature {temp}°C is perfect for plants!")
   
    
def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    
    print("Testing temperature: 25")
    try:
        check_temperature(*/*/*/*//*)
    except Exception as e:
        print(e)
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