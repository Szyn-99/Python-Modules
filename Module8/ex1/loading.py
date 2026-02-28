import importlib

def missing_dependecies_detector() -> bool:
    print("\nLOADING STATUS: Loading programs...\n")
    try:
        to_import = {'pandas': "Data manipulation", 'numpy': "Numerical computations", 'matplotlib': "Visualization"}
        dep = {}
        error = 0
        for module in to_import:
            try:
                imported = importlib.import_module(module)
                if imported:
                    dep.update({module: imported})
                    print(f"[OK] {module} ({getattr(imported, "__version__", "unknown version")}) - {to_import[module]} ready")
            except ImportError:
                print(f"[KO] {module} (unknown version) - {to_import[module]} not ready")
                error = 1
        if error == 1:
            exit(1)
        return dep
    except Exception as e:
        print("alo")
        raise

def testing_dependencies() -> None:
    try:
        dep = missing_dependecies_detector()
        matplotlib = importlib.import_module("matplotlib.pyplot")
        pandas = dep['pandas']
        numpy = dep['numpy']

        x = numpy.linspace(0, 10, 100)
        y = numpy.sin(x)

        df = pandas.DataFrame({'x': x, 'y': y})

        matplotlib.plot(df['x'], df['y'])
        matplotlib.title("Simple Sine Wave")
        matplotlib.xlabel("X values")
        matplotlib.ylabel("Y values")
        matplotlib.show()

    except Exception as e:
        print(f"Error: {e.__class__.__name__} - {e}")
        
    
testing_dependencies()