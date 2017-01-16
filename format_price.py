import re
from math import log10, modf
from argparse import ArgumentParser


def separate_price(price):
    separated_price = {'integer': None, 'fractional': ''}
    fractional, integer = modf(price)
    separated_price['integer'] = int(integer)
    if fractional:
        fractional = round(fractional, 2)
        if not fractional < 1:
            fractional = '0.99'
        separated_price['fractional'] = str(fractional).replace('0', '')
    return separated_price


def normalize_price(price):
    if isinstance(price, (int, float)):
        valid_price = separate_price(price)
        return valid_price
    if isinstance(price, str):
        if re.fullmatch('\d*[.,]?\d+', price):
            price = price.replace(',', '.')
            valid_price = separate_price(float(price))
            return valid_price
        raise ValueError('An input must match "[0-9].[0-9]" pattern!')
    raise TypeError('An input must be int, float or string matching "[0-9].[0-9]" pattern!')


def format_price(price):
    valid_price = normalize_price(price)
    price, formated_price = valid_price['integer'], str(valid_price['integer'])
    separation_grade = 1000
    insert_index = int(log10(separation_grade))
    index_shift = insert_index + 1
    price //= separation_grade
    while price:
        formated_price = '{} {}'.format(formated_price[:-insert_index], formated_price[-insert_index:])
        insert_index += index_shift
        price //= separation_grade
    formated_price += valid_price['fractional']
    return formated_price


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-p', '--price', nargs='?', required=True, dest='price',
                        help='Price to format')
    options = parser.parse_args()

    print(format_price(options.price))
