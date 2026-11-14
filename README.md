# Rational Wheels

Rational Wheels is a Python implementation of a wheel of rational numbers:

- canonical rational numbers;
- infinity (`∞`);
- nullity (`⊥`);
- total arithmetic operations, including division by zero.

## Installation

```bash
python -m pip install rational-wheels
```

## Quick start

```python
from rational_wheels import WheelQ

result = WheelQ(1, 2) + WheelQ(1, 3)
print(result)  # 5/6

print(WheelQ.inf())  # ∞
print(WheelQ.bot())  # ⊥
```

`WheelQ` accepts integers directly and supports addition, subtraction,
multiplication, division, negation, and multiplicative inversion:

```python
assert WheelQ(2, 4) == WheelQ(1, 2)
assert WheelQ(1, 0).is_inf()
assert (WheelQ(1) / 0).is_inf()
```

## Development

Install the build tool and create both distributable formats:

```bash
python -m pip install build
python -m build
```

The wheel and source distribution are written to `dist/`.

## Publishing

This repository includes GitHub Actions workflows for trusted publishing
without storing PyPI tokens:

- `.github/workflows/publish-testpypi.yml` publishes to TestPyPI;
- `.github/workflows/publish-pypi.yml` publishes to PyPI.

Configure a Trusted Publisher for each service with:

1. Project name: `rational-wheels`
2. Owner: the GitHub user or organization that owns this repository
3. Repository: this repository's name
4. Workflow: the exact workflow filename
5. Environment: `testpypi` for TestPyPI or `pypi` for PyPI

Create the corresponding GitHub environments before publishing. To publish
to PyPI, create a GitHub Release; TestPyPI can also be started manually from
the Actions tab or by pushing a version tag such as `v0.1.0`.

## License

Rational Wheels is released under the [MIT License](LICENSE).
