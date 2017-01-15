import unittest
from format_price import format_price


class PriceFormattingTestCase(unittest.TestCase):
    def testInteger(self):
        price = 12345678
        assert format_price(price) == '12 345 678'

    def testFloat(self):
        price = 1234.345
        assert format_price(price) == '1 234.35'
        price = 1234.567
        assert format_price(price) == '1 234.57'

    def testStr(self):
        price = '12345.678'
        assert format_price(price) == '12 345.68'
        price = '12345,34'
        assert format_price(price) == '12 345.34'

    def testFailure(self):
        failure_values = ['breakme', '123 45', '']
        for value in failure_values:
            with self.assertRaises(ValueError):
                format_price(value)

        failure_types = [{'price': 1234}, None]
        for type in failure_types:
            with self.assertRaises(TypeError):
                format_price(type)


if __name__ == '__main__':
    unittest.main()
