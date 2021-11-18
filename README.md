# Sphinx bug in documenting type aliases

In Sphinx v4.3.0 and Python 3.8.2, docstrings for type aliases are not captured for primitive aliases, but are for `typing.Union` aliases.

To produce, install Sphinx into your Python environmen (e.g., `pip install sphinx`), then:

```sh
cd docs
make html
```

Then view the generated html for the module at: `docs/build/html/testmod.html`.
The aliases `testmod.FieldInt` and `testmod.FieldInt2` are listed but their docstrings are not included.
