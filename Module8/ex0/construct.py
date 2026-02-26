import sys
import os
def construct() -> None:
    try:
        if sys.prefix == sys.base_prefix:
            print("MATRIX STATUS: You're still plugged in\n")
            print(f"Current Python: {sys.executable}")
            print("Virtual Environment: None detected\n")
            print("WARNING: You're in the global environment!")
            print("The machines can see everything you install.\n")
            print("To enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate     # On Unix")
            print("matrix_env")
            print("Scripts")
            print("activate    # On Windows\n")
            print("Then run this program again.")
        else:
            print(f"MATRIX STATUS: Welcome to the {os.path.basename(__file__).split('.')[0]}\n")
            print(f"Current Python: {sys.executable}")
            print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
            print(f"Environment Path: {sys.prefix}")
            print(
                "SUCCESS: You're in an isolated environment!"
                "Safe to install packages without affecting"
                " the global system.\n"
                )
            
            print(f"Package installation path:\n {sys.path[-1]}")
            
            
    except Exception as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    construct()
    # print(os.path)
