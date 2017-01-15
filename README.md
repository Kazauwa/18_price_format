# Price Formatter

A script for prettifying stored prices.

## Usage
#### CLI
```
python format_prices.py -p --price
```
#### Import
```
from format_price import format_price
```
An input must be an integer, float or a string matching integer or float format. If input is string representig float, then delimiter must be either dot or comma. Output result is formatted price.

## Parameters
-p --price - Input price to format

## Test
`python test.py` runs unittest.

## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
