def check_temperature(temp_str: str) -> None:
    try:
        try:
            temp = int(temp_str)
        except ValueError:
            raise ValueError(f"Error: '{temp_str}' is not a valid number")
        if temp < 0:
            raise ValueError(f"Error: {temp}°C is too cold for plants (min 0°C)")
        elif temp > 40:
            raise ValueError(f"Error: {temp}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
            return None
    except Exception as alo:
        print(alo)
        return None


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    print("Testing temperature: 25")
    try:
        check_temperature(402 / 10)
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()
    print("Testing temperature: abc")
    try:
        check_temperature("abc")
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()
    print("Testing temperature: 100")
    try:
        check_temperature("100")
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()
    print("Testing temperature: -50")
    try:
        check_temperature("-50")
    except Exception as subject_says_No_Crash:
        print(f"Subject Requirement: {subject_says_No_Crash}")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
