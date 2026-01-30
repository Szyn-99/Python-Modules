import sys
import math


def parsing_input_2(argvs: list) -> tuple:
    try:
        length = len(argvs) - 1
        if length == 1:
            cords = [int(i) for i in argvs[1].split(",")]
        elif length == 3:
            cords = [int(i) for i in argvs[1:]]
        elif length > 3:
            raise ValueError("Too many arguments")
        elif length < 3:
            raise ValueError("Not enough arguments")
        coordinate = tuple(cords)
    except Exception:
        raise
    return coordinate


def unpacking_coordinates(coordinates: tuple) -> None:
    print("Unpacking demonstration:")
    x, y, z = coordinates
    print(f"Player at: x={x}, y={y}, z={z}")
    print(f"Coordinates: X: {x}, Y: {y}, Z: {z}")


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    try:
        x, y, z = 0, 0, 0
        position = parsing_input_2(sys.argv)
        distance = math.sqrt(
            (position[0] - x) ** 2 + (position[1] - y) ** 2 +
            (position[2] - z) ** 2
        )
        print(f"Position created: {position}")
        print(
            f"Distance between ({x}, {y}, {z}) and {position}: "
            f"{distance:.2f}\n"
        )
        unpacking_coordinates(position)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(
            f'Error details - Type: {e.__class__.__name__}, '
            f'Args: ("{sys.argv[1:]}")'
        )


if __name__ == "__main__":
    ft_coordinate_system()
