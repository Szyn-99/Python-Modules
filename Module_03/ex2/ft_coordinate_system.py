import sys
import math


def get_len(argvs: list) -> int:
    i = 0
    for arg in argvs:
        i += 1
    return i

def parsing_input_2(argvs: list) -> tuple:
    try:
        length = get_len(argvs) - 1
        if(length == 1):
            cords = [int(i) for i in argvs[1].split(',')]
        elif length == 3:
            cords = [int(i) for i in argvs[1:]]
        elif length > 3:
            raise ValueError("Too many arguments")
        elif length < 3:
            raise ValueError("Not enough arguments") 
        Coordinate = tuple(cords)
    except Exception:
        raise
    return Coordinate

def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    try:
        position = parsing_input_2(sys.argv)
        distance = math.sqrt(position[0]**2 + position[1]**2 + position[2]**2)
        print(f"Position created: {position}")
        print(f"Distance between (0, 0, 0) and {position}: {distance:.2f}")
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {e.__class__.__name__}, Args: (\"{e}\")")

if __name__ == "__main__":
    ft_coordinate_system()