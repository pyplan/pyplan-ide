"""bootstrap.__main__: executed when bootstrap directory is called as script."""


import sys
from .pyplan_ide import main

if __name__ == "__main__":
    sys.exit(main())
