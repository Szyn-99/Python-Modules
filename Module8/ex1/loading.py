import importlib

def missing_dependecies_detector() -> bool:
    print("\nLOADING STATUS: Loading programs...\n")
    try:
        print("Checking dependencies:")
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
        data_points = 1000
        print("\nAnalyzing Matrix data...")
        numpy_x = numpy.array([x for x in range(data_points)])
        numpy_y = numpy.array([y for y in range(data_points)])
        print(f"Processing {data_points} data points...")
        structured_data = pandas.DataFrame({
            "panda_x": numpy_x,
            "panda_y": numpy_y
        })
        print("Generating visualization...")
        matplotlib.plot(structured_data["panda_x"], structured_data["panda_y"])
        print("\nAnalysis complete!")
        matplotlib.savefig("analysis.png")
        print("Results saved to: matrix\_analysis.png}")
        # matplotlib.show()

    except Exception as e:
        print(f"Error: {e.__class__.__name__} - {e}")
        
    
testing_dependencies()