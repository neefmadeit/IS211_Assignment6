import unittest
import conversions as conv

class TestCelsiusConversions(unittest.TestCase):
    def test_convertCelsiusToFahrenheit(self):
        cases = [
            (-40.0, -40.0),
            (0.0, 32.0),
            (100.0, 212.0),
            (37.0, 98.6),
            (300.0, 572.0),
        ]
        for c, expected in cases:
            with self.subTest(celsius=c):
                result = conv.convertCelsiusToFahrenheit(c)
                print(f"[C->F] {c} °C -> expected {expected} °F, got {result}")
                self.assertAlmostEqual(result, expected, places=2)

    def test_convertCelsiusToKelvin(self):
        cases = [
            (-273.15, 0.0),
            (-40.0, 233.15),
            (0.0, 273.15),
            (100.0, 373.15),
            (300.0, 573.15),
        ]
        for c, expected in cases:
            with self.subTest(celsius=c):
                result = conv.convertCelsiusToKelvin(c)
                print(f"[C->K] {c} °C -> expected {expected} K, got {result}")
                self.assertAlmostEqual(result, expected, places=2)


class TestFahrenheitConversions(unittest.TestCase):
    def test_convertFahrenheitToCelsius(self):
        cases = [
            (-40.0, -40.0),
            (32.0, 0.0),
            (212.0, 100.0),
            (98.6, 37.0),
            (572.0, 300.0),
        ]
        for f, expected in cases:
            with self.subTest(fahrenheit=f):
                result = conv.convertFahrenheitToCelsius(f)
                print(f"[F->C] {f} °F -> expected {expected} °C, got {result}")
                self.assertAlmostEqual(result, expected, places=2)

    def test_convertFahrenheitToKelvin(self):
        cases = [
            (-459.67, 0.0),
            (-40.0, 233.15),
            (32.0, 273.15),
            (212.0, 373.15),
            (572.0, 573.15),
        ]
        for f, expected in cases:
            with self.subTest(fahrenheit=f):
                result = conv.convertFahrenheitToKelvin(f)
                print(f"[F->K] {f} °F -> expected {expected} K, got {result}")
                self.assertAlmostEqual(result, expected, places=2)


class TestKelvinConversions(unittest.TestCase):
    def test_convertKelvinToCelsius(self):
        cases = [
            (0.0, -273.15),
            (233.15, -40.0),
            (273.15, 0.0),
            (373.15, 100.0),
            (573.15, 300.0),
        ]
        for k, expected in cases:
            with self.subTest(kelvin=k):
                result = conv.convertKelvinToCelsius(k)
                print(f"[K->C] {k} K -> expected {expected} °C, got {result}")
                self.assertAlmostEqual(result, expected, places=2)

    def test_convertKelvinToFahrenheit(self):
        cases = [
            (0.0, -459.67),
            (233.15, -40.0),
            (273.15, 32.0),
            (373.15, 212.0),
            (573.15, 572.0),
        ]
        for k, expected in cases:
            with self.subTest(kelvin=k):
                result = conv.convertKelvinToFahrenheit(k)
                print(f"[K->F] {k} K -> expected {expected} °F, got {result}")
                self.assertAlmostEqual(result, expected, places=2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
