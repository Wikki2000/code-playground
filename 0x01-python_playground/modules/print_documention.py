"""print_documentation.py

This script demonstrates how to print the documentation of a module and its functions.
"""

def print_module_documentation(module):
    """Print the documentation of a module.

    Args:
        module (module): The module object.

    """
    print("Documentation for module:", module.__name__)
    print(module.__doc__)

def print_function_documentation(module, function_name):
    """Print the documentation for a specific function within a module.

    Args:
        module (module): The module object.
        function_name (str): The name of the function.

    """
    function = getattr(module, function_name, None)
    if function:
        print("Documentation for function:", function_name)
        print(function.__doc__)
    else:
        print("Function", function_name, "not found in module", module.__name__)


