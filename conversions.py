"""Temperature conversions"""

def convertCelsiusToKelvin(c: float) -> float:
    """Convert Celsius to Kelvin.
    Formula: K = C + 273.15
    """
    return float(c) + 273.15

def convertCelsiusToFahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit.
    Formula: F = C * 9/5 + 32
    """
    return (float(c) * 9.0 / 5.0) + 32.0

def convertFahrenheitToCelsius(f: float) -> float:
    """Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) * 5/9
    """
    return (float(f) - 32.0) * 5.0 / 9.0

def convertFahrenheitToKelvin(f: float) -> float:
    """Convert Fahrenheit to Kelvin.
    Formula: K = (F - 32) * 5/9 + 273.15
    """
    return (float(f) - 32.0) * 5.0 / 9.0 + 273.15

def convertKelvinToCelsius(k: float) -> float:
    """Convert Kelvin to Celsius.
    Formula: C = K - 273.15
    """
    return float(k) - 273.15

def convertKelvinToFahrenheit(k: float) -> float:
    """Convert Kelvin to Fahrenheit.
    Formula: F = (K - 273.15) * 9/5 + 32
    """
    return (float(k) - 273.15) * 9.0 / 5.0 + 32.0
