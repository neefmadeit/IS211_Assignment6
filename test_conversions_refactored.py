import unittest
from conversions_refactored import convert, ConversionNotPossible

class TestRefactoredTemperature(unittest.TestCase):
    def test_all_temperature_conversions(self):
        values = [-40.0, 0.0, 37.0, 100.0, 300.0]
        pairs = [
            ('celsius', 'fahrenheit'), ('celsius', 'kelvin'),
            ('fahrenheit', 'celsius'), ('fahrenheit', 'kelvin'),
            ('kelvin', 'celsius'), ('kelvin', 'fahrenheit')
        ]
        for v in values:
            for frm, to in pairs:
                with self.subTest(value=v, frm=frm, to=to):
                    if frm == 'celsius' and to == 'fahrenheit':
                        expected = v * 9/5 + 32
                    elif frm == 'celsius' and to == 'kelvin':
                        expected = v + 273.15
                    elif frm == 'fahrenheit' and to == 'celsius':
                        expected = (v - 32) * 5/9
                    elif frm == 'fahrenheit' and to == 'kelvin':
                        expected = (v - 32) * 5/9 + 273.15
                    elif frm == 'kelvin' and to == 'celsius':
                        expected = v - 273.15
                    elif frm == 'kelvin' and to == 'fahrenheit':
                        expected = (v - 273.15) * 9/5 + 32
                    else:
                        raise AssertionError('Unexpected pair')
                    result = convert(frm, to, v)
                    print(f"[TEMP] {v} {frm} -> {to}: expected {expected}, got {result}")
                    self.assertAlmostEqual(result, expected, places=6)


class TestRefactoredDistance(unittest.TestCase):
    def test_all_distance_conversions(self):
        values = [0.0, 1.0, 5.5, 100.0, 1234.56]
        pairs = [
            ('miles', 'meters'), ('meters', 'miles'),
            ('yards', 'meters'), ('meters', 'yards'),
            ('miles', 'yards'), ('yards', 'miles'),
        ]
        meters_per = {'meters': 1.0, 'yards': 0.9144, 'miles': 1609.344}
        for v in values:
            for frm, to in pairs:
                with self.subTest(value=v, frm=frm, to=to):
                    meters = v * meters_per[frm]
                    expected = meters / meters_per[to]
                    result = convert(frm, to, v)
                    print(f"[DIST] {v} {frm} -> {to}: expected {expected}, got {result}")
                    self.assertAlmostEqual(result, expected, places=9)


class TestIdentityAndErrors(unittest.TestCase):
    def test_identity_all_units(self):
        units = ['celsius', 'fahrenheit', 'kelvin', 'meters', 'yards', 'miles']
        values = [-40.0, 0.0, 3.14, 42.0, 1000.001]
        for u in units:
            for v in values:
                with self.subTest(unit=u, value=v):
                    result = convert(u, u, v)
                    print(f"[ID] {v} {u} -> {u}: expected {v}, got {result}")
                    self.assertEqual(result, v)

    def test_incompatible_units_raise(self):
        bad_pairs = [
            ('celsius', 'meters'), ('kelvin', 'yards'),
            ('miles', 'fahrenheit'), ('yards', 'celsius'),
        ]
        for frm, to in bad_pairs:
            with self.subTest(frm=frm, to=to):
                print(f"[ERR] Expecting ConversionNotPossible for {frm} -> {to}")
                with self.assertRaises(ConversionNotPossible):
                    convert(frm, to, 1.23)


if __name__ == '__main__':
    unittest.main(verbosity=2)
