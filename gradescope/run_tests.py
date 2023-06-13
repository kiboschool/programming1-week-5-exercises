import os
import sys
import unittest
import fnmatch
import importlib
import inspect
import types
import functools
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

from importlib.abc import MetaPathFinder

def _modify_sys_path(test_dir):
    """
    Decorator function to modify sys.path for a test case so that it
    explicitly includes it's own directory in the path.  E.g., if the
    `test_main.py` is in a subdirectory `ac-load-estimator`, `ac-load-estimator`
    is explicitly added to sys.path so that the corresponding solution
    in that directory (`main.py`) can be loaded.  The directory is 
    removed from the path after the test case runs to avoid conflicting 
    with other `main.py` in other subdirectories.
    """
    def decorator(test_func):
        @functools.wraps(test_func)
        def wrapper(*args, **kwargs):
            # Add the test directory to sys.path
            sys.path.insert(0, test_dir)
            # Run the test case
            result = test_func(*args, **kwargs)
            # Remove the test directory from sys.path
            sys.path.remove(test_dir)
            return result

        return wrapper
    return decorator

def _apply_decorator_to_test_functions(module, decorator):
    """
    Decorate all of the `test*` methods in any unittest.TestCase classes 
    contained in the module.
    """
    for name in dir(module):
        obj = getattr(module, name)
        if inspect.isclass(obj) and issubclass(obj, unittest.TestCase):
            _apply_decorator_to_test_functions(obj, decorator)
        elif isinstance(obj, types.FunctionType) and name.startswith('test'):
            setattr(module, name, decorator(obj))


class MultiDirectoryTestLoader(unittest.TestLoader):

    def loadTestsFromModule(self, module, *args, pattern=None, **kws):
        """Load tests from the given module and apply decorators."""
        # Get the directory of the current test module
        test_dir = os.path.dirname(module.__file__)
        _apply_decorator_to_test_functions(module, _modify_sys_path(test_dir))
        return super().loadTestsFromModule(module)

    def discover(self, start_dir, pattern='test*.py'):
        """Override the discover method to load tests from multiple subdirectories."""
        tests = []
        for root, _, _ in os.walk(start_dir):
            if pattern.startswith('*.'):
                pattern = pattern[1:]
            for file in os.listdir(root):
                if fnmatch.fnmatch(file, pattern):
                    rel_path = os.path.relpath(root, start_dir)
                    module_name = rel_path + '.' + os.path.splitext(file)[0]
                    module = importlib.import_module(module_name)
                    tests.append(self.loadTestsFromModule(module))
        return self.suiteClass(tests)


if __name__ == '__main__':

    # Create a test suite using the MultiDirectoryTestLoader
    loader = MultiDirectoryTestLoader()
    suite = loader.discover('.')

    # Gradescope wants the results.json file in /autograder/results/
    # but when testing locally, more convenient for it to be in current
    # directory.
    results = 'results.json'
    if os.path.exists('/autograder/results'):
        results = '/autograder/results/' + results
    with open(results, 'w') as f:
        JSONTestRunner(visibility='visible', stream=f).run(suite)
