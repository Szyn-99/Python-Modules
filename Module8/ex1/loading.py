# import pandas
# import numpy
# import matplotlib
import importlib


def missing_dependecies_detector() -> bool:
    try:
        to_import = ['pandas', 'numpy', 'matplotlib']
        dependency_and_version = []
        for module in to_import:
            try:
                imported = importlib.import_module(module)
                if imported:
                    dependency_and_version.append([(imported, imported.__name__, imported.__version__)])
                    to_import.pop(0)
            
            except ImportError:
                return False, dependency_and_version
        return True, dependency_and_version
    except Exception as e:
        print(f"Error: {e.__class__.__name__} - {e}")

def testing_dependencies() -> None:
    try:
        a = missing_dependecies_detector()
        missing , dependency_and_version = a
    except Exception as e:
        print(f"Error: {e.__class__.__name__} - {e}")
        
    
testing_dependencies()