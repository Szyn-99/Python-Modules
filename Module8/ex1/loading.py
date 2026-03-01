import importlib
from types import ModuleType


def missing_dependecies_detector() -> dict[str, ModuleType]:
    """Check for required dependencies
    and return successfully imported modules."""

    print("\nLOADING STATUS: Loading programs...\n")
    try:
        print("Checking dependencies:")
        to_import = {
            'pandas': "Data manipulation",
            'numpy': "Numerical computations",
            'matplotlib': "Visualization",
        }
        dep = {}
        error = False
        for module in to_import:
            try:
                imported = importlib.import_module(module)
                if imported:
                    dep.update({module: imported})
                    print(
                        f"[OK] {module} "
                        f"({getattr(imported, '__version__', 'None')})"
                        f" - {to_import[module]} ready"
                    )
            except ImportError:
                print(
                    f"[KO] {module} (unknown version)"
                    f" - {to_import[module]} not ready"
                )
                error = True
        if error:
            print("\nInstallation instructions:")
            print(f"Poetry: poetry install {' '.join(to_import.keys())}")
            print(f"Pip: pip install {' '.join(to_import.keys())}")
            exit(1)
        return dep
    except Exception:
        raise


def testing_dependencies() -> None:
    try:
        """Run a sample analysis using loaded
        dependencies and saves the result."""
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
            "panda_y": numpy_y,
        })
        print("Generating visualization...")
        matplotlib.plot(structured_data["panda_x"], structured_data["panda_y"])
        print("\nAnalysis complete!")
        save_path = "analysis.png"
        matplotlib.savefig(save_path)
        print(f"Results saved to: {save_path}")

    except Exception as e:
        print(f"Error: {e.__class__.__name__} - {e}")


if __name__ == "__main__":
    testing_dependencies()
