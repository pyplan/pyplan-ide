#!/usr/bin/env python
import os
import sys

import environ

if __name__ == "__main__":

    # set default variables
    os.environ.setdefault("PYPLAN_IDE", "1")
    os.environ.setdefault("DJANGO_SECRET_KEY",
                          "u3aSy6*vvC&8shi-3kpq6ii2r@ga^kr2v02jb7lcha%()td]")
    os.environ.setdefault("DEBUGGING_HOST", "localhost")
    os.environ.setdefault("LOCAL_CODE_FOLDER", ".")

    os.environ.setdefault("DJANGO_SECRET_KEY_ENGINE.",
                          "u3!a&y6*vv%&8shi-3kpq6ii2r@ga^k!r2v02jb7lcha%()td)")
    os.environ.setdefault("DJANGO_CONFIGURATION_ENGINE", "Production")
    os.environ.setdefault("USE_MULTIPROCESS", "0")
    os.environ.setdefault("FREE_MEMORY_FOR_NEW_SESSION", "0.5")
    os.environ.setdefault("MAX_MEMORY_FOR_SESSION", "64")
    os.environ.setdefault("PYPLAN_API_HOST", "http://localhost:9740/api")

    # read .env file
    if os.path.isfile('.env'):
        environ.Env.read_env(env_file='.env')

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyplan.config.settings")
    os.environ.setdefault("DJANGO_CONFIGURATION", "Local")
    try:
        from configurations.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django  # noqa
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
