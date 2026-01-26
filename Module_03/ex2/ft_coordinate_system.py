import sys
import math

# def parsing_input(position: list) -> tuple:
#     i = len(sys.argv[1:])
#     if i == 3:
#         Coordinate = tuple(position[1:])
#     elif i > 3:
#         raise ValueError("Too many arguments")
#     elif i < 3:
#         raise ValueError("Not enough arguments")
#     return Coordinate
            
  
def parsing_input_2(position: list) -> tuple:
    try:
        cords = [int(i) for i in position]
        Coordinate = tuple(cords)
    except ValueError:
        raise ValueError("Invalid data, only floats/ints acceptable")
    return Coordinate

def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    try:
        position = parsing_input_2(sys.argv[1].split(','))
        distance = math.sqrt(position[0]**2 + position[1]**2 + position[2]**2)
        print(f"Position created: {position}")
        print(f"Distance between (0, 0, 0) and {position}: {distance:.2f}")
        
    except Exception as e:
        print(f"Error: {e}")

ft_coordinate_system()


