import re
from math import log10
from argparse import ArgumentParser


def prepare_input(price):
    if isinstance(price, (int, float)):
        return round(price)
    if isinstance(price, str):
        if price.isdigit():
            return int(price)
        if re.fullmatch('\d*[.,]?\d+', price):
            price = price.replace(',', '.')
            price = float(price)
            return round(price)
        raise ValueError('An input must match "[0-9].[0-9]" pattern!')
    raise TypeError('An input must be int, float or string matching "[0-9].[0-9]" pattern!')


def format_price(price, separation_grade=1000):
    price = prepare_input(price)
    formated_price = str(price)
    insert_index = int(log10(separation_grade))
    index_shift = insert_index + 1
    price //= separation_grade
    while price:
        formated_price = '{} {}'.format(formated_price[:-insert_index], formated_price[-insert_index:])
        insert_index += index_shift
        price //= separation_grade
    return formated_price


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-p', '--price', nargs='?', required=True, dest='price',
                        help='Price to format')
    parser.add_argument('-g', '--grade', type=int, nargs='?', default=1000,
                        help='Separation grade. Must be a power of ten.')
    options = parser.parse_args()

    print(format_price(price=options.price))
