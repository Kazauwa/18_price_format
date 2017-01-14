import unittest
from format_price import format_price


class PriceFormattingTestCase(unittest.TestCase):
    def testInteger(self):
        price = 12345678
        assert format_price(price) == '12 345 678'
        assert format_price(price, separation_grade=1000000) == '12 345678'

    def testFloat(self):
        price = 1234.345
        assert format_price(price) == '1 234'
        price = 1234.567
        assert format_price(price) == '1 235'

    def testStr(self):
        price = '12345.678'
        assert format_price(price) == '12 346'
        price = '12345,34'
        assert format_price(price) == '12 345'

    def testFailure(self):
        with self.assertRaises(ValueError):
            price = 'breakme'
            format_price(price)
            price = '123 45'
            format_price(price)
            price = str()
            format_price(price)

        with self.assertRaises(TypeError):
            price = {'price': 1234}
            format_price(price)


if __name__ == '__main__':
    unittest.main()
