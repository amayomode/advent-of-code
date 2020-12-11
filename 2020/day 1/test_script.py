import pytest
from script import two_entries


def get_values(s):
    record, ans = s.split('-')
    return [int(num.strip()) for num in record.split(',')], int(ans.strip())


def test_script():
    with open('test_cases.txt', 'r') as file:
        for line in file.readlines():
            record, ans = get_values(line)
            assert two_entries(record) == ans, 'test failed'
