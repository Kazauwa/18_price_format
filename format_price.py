import re
from math import modf
from argparse import ArgumentParser


def normalize_price(price):
    if isinstance(price, (int, float)):
        return float(price)
    if isinstance(price, str):
        if re.fullmatch('\d*[.,]?\d+', price):
            price = price.replace(',', '.')
            return float(price)
        raise ValueError('An input must match "[0-9].[0-9]" pattern!')
    raise TypeError('An input must be int, float or string matching "[0-9].[0-9]" pattern!')


def normalize_fractional(fractional):
    if not fractional:
        return ''
    fractional = '{:.2f}'.format(fractional)
    if not float(fractional) < 1:
        # we don't want our fraction rounded to 1.0 if it's somewhere around 0.99
        fractional = '.99'
    fractional = fractional.lstrip('0')
    return fractional


def format_price(price):
    valid_price = normalize_price(price)
    fractional, integer = modf(valid_price)
    valid_fractional = normalize_fractional(fractional)
    formated_price = '{:,.0f}'.format(integer)
    formated_price = formated_price.replace(',', ' ')
    formated_price += valid_fractional
    return formated_price


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-p', '--price', nargs='?', required=True, dest='price',
                        help='Price to format')
    options = parser.parse_args()

    print(format_price(options.price))
