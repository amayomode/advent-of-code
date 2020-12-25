from part1 import extract_passwords, isvalid
import re


def parse_password(password: str) -> dict:
    keys = {}
    for field in password.split():
        k, v = field.split(':')
        keys[k] = v
    return keys


def validate_years(password: dict) -> bool:
    byr = password['byr']
    iyr = password['iyr']
    eyr = password['eyr']

    def check_if_num(num): return num.isdecimal()
    def check_if_four(num): return len(num) == 4

    def validate_byr(num): return 1920 <= int(num) <= 2002
    def validate_iyr(num): return 2010 <= int(num) <= 2020
    def validate_eyr(num): return 2020 <= int(num) <= 2030

    if not all(map(check_if_four, (byr, iyr, eyr))):
        return False
    if not all((validate_byr(byr), validate_iyr(iyr), validate_eyr(eyr))):
        return False

    return True


def validate_height(password: dict) -> bool:
    hgt = password['hgt']
    if re.match(r'^\d+(in|cm)$', hgt):
        val = int(hgt[:-2])
        unit = hgt[-2:]
        if unit == 'cm':
            return 150 <= val <= 193
        elif unit == 'in':
            return 59 <= val <= 76
        else:
            return False
    else:
        return False
    return True


def validate_hair_color(password: dict) -> bool:
    if re.match(r'^#([0-9]|[a-f]){6}', password['hcl']):
        return True
    return False


def validate_eye_color(password: dict) -> bool:
    return password['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def validate_pass_id(password: dict) -> bool:
    pid = password['pid']
    if pid.isdigit() and len(pid) == 9:
        return True
    return False


def validate_password(password: dict) -> bool:
    tests = (validate_years, validate_height, validate_hair_color,
             validate_eye_color, validate_pass_id)
    keys = set(password.keys())
    if isvalid(keys):
        for test in tests:
            if not test(password):
                return False
    else:
        return False
    return True


def count_valid(passwords: list) -> int:
    count = 0
    for password in passwords:
        test = parse_password(password)
        if validate_password(test):
            count += 1
    return count


if __name__ == '__main__':
    passwords = extract_passwords('input.txt')
    print(count_valid(passwords))
