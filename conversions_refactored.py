"""Generalized unit conversion supporting temperature (Celsius, Fahrenheit, Kelvin)
and distance (Miles, Yards, Meters). Includes a single entry point `convert` and
an exception `ConversionNotPossible` for incompatible unit categories."""

from typing import Callable, Dict, Tuple

class ConversionNotPossible(Exception):
    """Raised when trying to convert between incompatible unit categories."""
    pass

# Normalize unit names to a canonical token
_UNIT_ALIASES = {
    'c': 'celsius', 'celsius': 'celsius', 'celcius': 'celsius',
    'f': 'fahrenheit', 'fahrenheit': 'fahrenheit',
    'k': 'kelvin', 'kelvin': 'kelvin',
    'm': 'meters', 'meter': 'meters', 'meters': 'meters', 'metre': 'meters', 'metres': 'meters',
    'yd': 'yards', 'yard': 'yards', 'yards': 'yards',
    'mi': 'miles', 'mile': 'miles', 'miles': 'miles',
}

# Temperatures use affine transforms to/from the base (Kelvin).
_TEMPERATURE: Dict[str, Tuple[Callable[[float], float], Callable[[float], float]]] = {
    'celsius': (
        lambda c: c + 273.15,            # to Kelvin
        lambda k: k - 273.15             # from Kelvin
    ),
    'fahrenheit': (
        lambda f: (f - 32.0) * 5.0/9.0 + 273.15,    # to Kelvin
        lambda k: (k - 273.15) * 9.0/5.0 + 32.0     # from Kelvin
    ),
    'kelvin': (
        lambda k: k,                     # to Kelvin
        lambda k: k                      # from Kelvin
    ),
}

# Distances use linear scaling to/from the base (Meters).
_METERS_PER_UNIT: Dict[str, float] = {
    'meters': 1.0,
    'yards': 0.9144,
    'miles': 1609.344,
}


def _normalize(unit: str) -> str:
    try:
        return _UNIT_ALIASES[unit.strip().lower()]
    except Exception:
        # Not a known unit at all; treat as incompatible to anything but itself
        return unit.strip().lower()


def convert(fromUnit: str, toUnit: str, value: float) -> float:
    """Convert *value* from *fromUnit* to *toUnit*.

    Supports temperature (Celsius, Fahrenheit, Kelvin) and distance (Miles, Yards, Meters)."""
    v = float(value)
    f_u = _normalize(fromUnit)
    t_u = _normalize(toUnit)

    # Identity conversion
    if f_u == t_u:
        return v

    # Temperature domain
    if f_u in _TEMPERATURE and t_u in _TEMPERATURE:
        to_base, _ = _TEMPERATURE[f_u]
        _, from_base = _TEMPERATURE[t_u]
        k = to_base(v)          # convert to Kelvin
        return from_base(k)     # convert Kelvin to target

    # Distance domain
    if f_u in _METERS_PER_UNIT and t_u in _METERS_PER_UNIT:
        meters = v * _METERS_PER_UNIT[f_u]
        return meters / _METERS_PER_UNIT[t_u]

    # If we get here, categories are incompatible (or unknown)
    raise ConversionNotPossible(f"Cannot convert from '{fromUnit}' to '{toUnit}'.")
