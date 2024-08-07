from re import findall


class NameTooShortError(Exception):
    ...


class MustContainAtSymbolError(Exception):
    ...


class InvalidDomainError(Exception):
    ...


class MoreThanOneAtSymbol(Exception):
    ...


class InvalidNameError(Exception):
    ...


VALID_DOMAINS = ('com', 'bg', 'org', 'net')
MIN_NAME_SYMBOLS = 4
pattern_name = r'\w+'

email = input()

while email != 'End':
    if email.count('@') > 1:
        raise MoreThanOneAtSymbol('Email should contain only one "@" symbol!')

    elif '@' not in email:
        raise MustContainAtSymbolError('Email must contain "@"!')

    elif len(email.split('@')[0]) <= MIN_NAME_SYMBOLS:
        raise NameTooShortError('Name must be more than 4 characters!')

    elif email.split('.')[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(
            f'Domain must be one of the following: {', '.join('.' + domain for domain in VALID_DOMAINS)}')

    elif findall(pattern_name, email.split('@')[0])[0] != email.split('@')[0]:
        raise InvalidNameError('Name must contain only letters, digits and underscores!')

    print('Email is valid')

    email = input()
