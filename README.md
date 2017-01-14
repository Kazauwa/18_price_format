# Price Formatter

A script for prettifying stored prices.

## Usage
#### CLI
```
python format_prices.py -p --price [-d --degree]
```
#### Import
```
from format_price import format_price
```
An input must be an integer, float or a string matching integer or float format. If input is string representig float, then delimiter must be either dot or comma. Output result is formatted price.

## Parameters
-p --price - Input price to format
-d --degree - Separation degree, must be a power of ten. 
#### Example
```
$ python format_price.py -p 1234567 -d 1000000
> 1 234567 
```

## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
