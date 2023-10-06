# adv_pwd_check

Enchanced Password Strength Check and Risk Assessment Tool.

## Description

The general idea is to allow a user to test various passwords to see how they pass or fail this analysis, in the hopes that said user will pick better password in the future.

## Prerequisites

This program requires Python 3.6+ (preferably 3.7+) and the following modules:

* sys
* string
* argparse
* zxcvbn (use pip3 to install this module)

## How to Use

This program rather simple and largely self-explanatory:

```
usage: pwd-check.py [-h] --password PASSWORD [--length LENGTH]

options:
  -h, --help            show this help message and exit
  --password PASSWORD, -p PASSWORD
                        password string to test
  --length LENGTH, -l LENGTH
                        minimum acceptible password length
```

This program will return (standard) values of 0 for success and 1 for failure.

## Exmaples

An example of an "acceptible" password:
```
$ ./pwd-check.py -p "TW89Q3h+dTZ0"

PASS: Password meets basic requirement.
INFO: Complexity value: 12
PASS: Password is suffiently complex.
INFO: Risk score: 4 - very low risk
PASS: Password is low risk.
```

An example of an "unacceptible" password (note the failures given):
```
$ ./pwd-check.py -p "P@ssw0rd1234"

PASS: Password meets basic requirements.
INFO: Complexity value: 4
FAIL: Password is not suffiently complex.
INFO: Risk score: 1 - high risk
FAIL: Password is unacceptibly risky.
```

## Fair Warning

Use at your own risk:
* Like any security-related product, you are assuming an unknown level of potential risk and liability.
* Neither warranty (expressed or implied) nor statement of suitability will be issued for this program.
* Never use any security product without prior testing, knowledge of it's limitations and compliance with your preferred/required acceptance criteria.

## Built With

* [Python](https://www.python.org/) Designed by Guido van Rossum.
* [zxcvbn](https://github.com/dropbox/zxcvbn) released by [dropbox.com](https://dropbox.com/)

## Author

**Rick Pelletier**

## License

See LICENSE file in this repo.
