import math
from typing import Union


class WheelQ:
    """
    Implementation of the Q_w abstract data type (wheel of rational numbers).
    Canonical SFP_w representation:
      - finite rationals: (n, m), with m > 0 and gcd(n, m) == 1
      - infinity (∞): (1, 0)
      - nullity (⊥): (0, 0)
    """
    __slots__ = ("n", "m")

    def __init__(self, n: int, m: int = 1):
        g = math.gcd(n, m)
        if g == 0:
            self.n, self.m = 0, 0
        else:
            n //= g
            m //= g
            if m < 0:
                n, m = -n, -m
            elif m == 0:
                n = 1
            self.n, self.m = n, m

    @classmethod
    def inf(cls) -> "WheelQ":
        return cls(1, 0)

    @classmethod
    def bot(cls) -> "WheelQ":
        return cls(0, 0)

    def is_bot(self) -> bool:
        return self.n == 0 and self.m == 0

    def is_inf(self) -> bool:
        return self.n == 1 and self.m == 0

    def is_finite(self) -> bool:
        return self.m > 0

    def inv(self) -> "WheelQ":
        """Return the multiplicative inverse x^-1."""
        return WheelQ(self.m, self.n)

    def __neg__(self) -> "WheelQ":
        return WheelQ(-self.n, self.m)

    def __add__(self, other: Union["WheelQ", int]) -> "WheelQ":
        if isinstance(other, int):
            other = WheelQ(other, 1)
        return WheelQ(self.n * other.m + self.m * other.n, self.m * other.m)

    def __radd__(self, other: int) -> "WheelQ":
        return self.__add__(other)

    def __sub__(self, other: Union["WheelQ", int]) -> "WheelQ":
        if isinstance(other, int):
            other = WheelQ(other, 1)
        return self + (-other)

    def __rsub__(self, other: int) -> "WheelQ":
        return WheelQ(other, 1) - self

    def __mul__(self, other: Union["WheelQ", int]) -> "WheelQ":
        if isinstance(other, int):
            other = WheelQ(other, 1)
        return WheelQ(self.n * other.n, self.m * other.m)

    def __rmul__(self, other: int) -> "WheelQ":
        return self.__mul__(other)

    def __truediv__(self, other: Union["WheelQ", int]) -> "WheelQ":
        """Perform total division: x / y = x * y^-1."""
        if isinstance(other, int):
            other = WheelQ(other, 1)
        return self * other.inv()

    def __rtruediv__(self, other: int) -> "WheelQ":
        return WheelQ(other, 1) / self

    def __eq__(self, other: object) -> bool:
        if isinstance(other, int):
            other = WheelQ(other, 1)
        if not isinstance(other, WheelQ):
            return False
        return self.n == other.n and self.m == other.m

    def __repr__(self) -> str:
        if self.m == 0:
            return "∞" if self.n == 1 else "⊥"
        if self.m == 1:
            return str(self.n)
        return f"{self.n}/{self.m}"
