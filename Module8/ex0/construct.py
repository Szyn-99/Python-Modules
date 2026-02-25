import sys
import os
def construct() -> None:
    try:
        if sys.prefix == sys.base_prefix:
            print("MATRIX STATUS: You're still plugged in")
            print(f"Current Python: {sys.executable}")
            print("Virtual Environment: None detected")
            print("WARNING: You're in the global environment!")
            print("The machines can see everything you install.")
            print("To enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate     # On Unix")
            print("matrix_env")
            print("Scripts")
            print("activate    # On Windows" )
            print("Then run this program again.")
        else:
            print(f"MATRIX STATUS: Welcome to the {os.path.basename(__file__).split('.')[0]}")
            print(f"Current Python: {sys.executable}")
            print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
            print(f"Environment Path: {sys.prefix}")
            print(
                "SUCCESS: You're in an isolated environment!\n"
                "Safe to install packages without affecting"
                " the global system."
                )
            
            print(f"Package installation path: {sys.path}")
            
            
    except Exception as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    construct()
    # print(os.path)
