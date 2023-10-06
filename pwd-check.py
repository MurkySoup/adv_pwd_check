#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Password Strength and Risk Check, Version 0.9.3-20231006-beta (do not distribute)
By Rick Pelletier (galiagante@gmail.com), 11 April 2022
Last update: 06 October 2023

Basic password risk analyzer using 'zxcvbn' with simple command-line interface.

See:
- https://github.com/dropbox/zxcvbn

Notes:

Pre-Check Conditions (can be easily custmozed)

- Password has minimumlength of 12 chacacters.
- Password contains at least one lower case letter.
- Password contains at least one upper case letter.
- Password contains at least one number.
- Password contains at least one special character.

Complexity Values:

- High numbers are good numbers.
- Values under 11-12 are risky enough to be actively avoided. This can probably be used as a pass/fail threshold.
- Values over 14-16 are generally representitive acceptible passwords.
- values over 16-18 are generally representitive pretty good passwords.
- Values over 22-24 are generally representitive "Fort Knox" passwords.

Risk Scores:

0 - extreme high risk. very easily (even trivially) guessable.
1 - high risk. guessable with amateur-level resources.
2 - moderate risk. guessable with better-than-average resources.
3 - low risk. guessable given significant resources.
4 - very low risk. guessable if large amounts of time, money and resources are not an issue.
"""


import sys
import string
import argparse
from zxcvbn import zxcvbn


def check_length(password: str, pwd_len: int) -> bool:
    if len(password) >= pwd_len:
        return True
    else:
        return False


def check_lowercase(password: str) -> bool:
    return any(char.islower() for char in password)


def check_uppercase(password: str) -> bool:
    return any(char.isupper() for char in password)


def check_numbers(password: str) -> bool:
    return any(char.isdigit() for char in password)


def check_special(password: str) -> bool:
    special_chars = r"""`~!@#$%^&*()_-+={[}}|\:;"'<,>.?/"""
    return any(char in special_chars for char in password)


def pre_checks(password: str, pwd_len: int) -> bool:
    if check_length(password, pwd_len) is False:
        print(f'FAIL: Password is less than {pwd_len} characters.')
        return False

    if check_lowercase(password) is False:
        print('FAIL: Password contains no lowercase letters.')
        return False

    if check_uppercase(password) is False:
        print('FAIL: Password contains no uppercase letters.')
        return False

    if check_numbers(password) is False:
        print('FAIL: Password contains no numbers.')
        return False

    if check_special(password) is False:
        print('FAIL: Password contains no special characters.')
        return False

    return True


def strength_test(password: str) -> tuple[float, int]:
    try:
        results = zxcvbn(password)
    except Exceptions as e:
        print(f'FAIL: Error condition - {e}')
        return False

    return results['guesses_log10'], results['score']


if __name__ == '__main__':
    exit_value = 0
    risk_rating = ['extreme high risk', 'high risk', 'moderate risk', 'low risk', 'very low risk']

    parser = argparse.ArgumentParser()
    parser.add_argument('--password', '-p', type=str, required=True, help='password string to test')
    parser.add_argument('--length', '-l', type=int, default=12, required=False, help='minimum acceptible password length')
    args = parser.parse_args()

    print()

    if flag := pre_checks(args.password, args.length):
        print('PASS: Password meets basic requirements.')
    else:
        print('FAIL: Password does not meet basic requirements.')
        exit_value = 1

    complexity_value, risk_score = strength_test(args.password)

    if complexity_value is not False:
        print(f'INFO: Complexity value: {int(complexity_value)}')

        if complexity_value >= 11:
            print('PASS: Password is suffiently complex.')
        else:
            print('FAIL: Password is not suffiently complex.')
            exit_value = 1
    else:
        print('FAIL: Complexity value unavailable.')
        exit_value = 1

    if risk_score is not False:
        print(f'INFO: Risk score: {risk_score} - {risk_rating[risk_score]}')

        if risk_score >= 3:
            print('PASS: Password is low risk.')
        else:
            print('FAIL: Password is unacceptibly risky.')
            exit_value = 1
    else:
        print('FAIL: Risk score unavailable.')
        exit_value = 1

    print()

    sys.exit(exit_value)
else:
    sys.exit(1)

# end of script
