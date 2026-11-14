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

## License

Rational Wheels is released under the [MIT License](LICENSE).
