import re


def verify(isbn):
    isbn = isbn.replace('-', '')

    if re.match('^\d-?\d{3}-?\d{5}-?[\dX]$', isbn):
        return check_digit_valid(isbn)
    else:
        return False


def check_digit_valid(isbn):
    sum = 0
    for(idx, digit) in enumerate(isbn):
        if digit == 'X':
            digit = 10
        else:
            digit = int(digit)

        sum += digit * (10 - idx)

    return sum % 11 == 0
