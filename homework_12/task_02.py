import re


def is_date(string: str) -> bool:
    return re.fullmatch(r'\d{2}-\d{2}-\d{4}', string) is not None


assert is_date('01-12-2022')
assert is_date('26-03-2020')
assert not is_date('253-05-2008')
assert not is_date('37-0o-2002')
