"""Simple entrypoint for the ml-course project."""

def main():
    info = {
        "ok": True,
    }
    try:
        import numpy as np
        import pandas as pd
        info["numpy"] = np.__version__
        info["pandas"] = pd.__version__
    except Exception:
        # packages may not be installed yet
        info["numpy"] = None
        info["pandas"] = None
    print("ml-course: OK")
    print(info)
    return True


if __name__ == "__main__":
    main()
