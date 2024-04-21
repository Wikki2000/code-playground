import os
import sys

def add_sibling_to_path(sibling_directory: str):
    """
    Add a sibling directory to the Python path.

    This function modifies the Python path to include a specified sibling directory,
    allowing modules from that directory to be imported directly. It is intended
    for use within package directories to facilitate importing modules from sibling
    directories.

    Args:
        sibling_directory (str): The name of the sibling directory to be added to
            the Python path.

    Returns:
        None
    """
    # Step 1: Get the current directory of the package
    current_file = __file__  # Use __file__ directly, no need for os.path.abspath
    package_dir = os.path.dirname(current_file)

    # Get the absolute path to the sibling directory
    sibling_dir = os.path.abspath(os.path.join(package_dir, '..', sibling_directory))

    # Add the sibling directory to the Python path
    sys.path.append(sibling_dir)

