def check_temperature(temp_str: str) -> int | None:
    try:
        try:
            temp = int(temp_str)
        except ValueError:
            raise ValueError(f"Error: '{temp_str}' is not a valid number")
        if temp < 0:
            raise ValueError(
                f"Error: {temp}°C is too cold for plants (min 0°C)")
        elif temp > 40:
            raise ValueError(
                f"Error: {temp}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
            return temp
    except Exception as alo:
        print(alo)


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    try:
        tmp = "25"
        print(f"Testing temperature: {tmp}")
        check_temperature(tmp)
    except Exception as error:
        print(f"Subject Requirement: {error}")
    print()
    try:
        tmp = "abc"
        print(f"Testing temperature: {tmp}")
        check_temperature(tmp)
    except Exception as error:
        print(f"Subject Requirement: {error}")
    print()
    try:
        tmp = "100"
        print(f"Testing temperature: {tmp}")
        check_temperature(tmp)
    except Exception as error:
        print(f"Subject Requirement: {error}")
    print()
    try:
        tmp = "-50"
        print(f"Testing temperature: {tmp}")
        check_temperature(tmp)
    except Exception as error:
        print(f"Subject Requirement: {error}")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
