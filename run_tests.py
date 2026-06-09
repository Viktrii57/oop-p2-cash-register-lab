#!/usr/bin/env python3
import sys
import importlib
import io
import traceback

# Ensure tests can import modules from lib
sys.path.insert(0, 'lib')

module_name = 'testing.cash_register_test'
mod = importlib.import_module(module_name)

TestClass = getattr(mod, 'TestCashRegister')

results = []

# Run test methods in the order they are defined in the class
for name, member in TestClass.__dict__.items():
    if name.startswith('test_'):
        # create new instance per test (pytest creates a new instance per test)
        instance = TestClass()
        func = getattr(instance, name)
        if callable(func):
            # capture stdout
            old_stdout = sys.stdout
            buf = io.StringIO()
            sys.stdout = buf
            try:
                func()
            except AssertionError:
                sys.stdout = old_stdout
                tb = traceback.format_exc()
                results.append((name, False, buf.getvalue(), tb))
            except Exception:
                sys.stdout = old_stdout
                tb = traceback.format_exc()
                results.append((name, False, buf.getvalue(), tb))
            else:
                sys.stdout = old_stdout
                results.append((name, True, buf.getvalue(), None))

# Print summary
passed = sum(1 for r in results if r[1])
failed = [r for r in results if not r[1]]
print(f"Ran {len(results)} tests: {passed} passed, {len(failed)} failed")
for name, ok, out, tb in results:
    status = 'PASS' if ok else 'FAIL'
    print(f"\n{name}: {status}")
    if out:
        print('Captured output:')
        print(out)
    if tb:
        print('Traceback:')
        print(tb)

if failed:
    sys.exit(1)
else:
    sys.exit(0)
