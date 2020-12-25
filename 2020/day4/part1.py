def extract_passwords(fname: str) -> list:
    with open(fname, 'r') as file:
        password = ''
        count = 0
        for line in file.readlines():
            password += ' ' + line.strip()
    return password.strip().split('  ')


def parse_password(password: str) -> set:
    keys = set()
    for field in password.split():
        keys.add(field.split(':')[0])
    return keys


def isvalid(keys: set) -> bool:
    fields = {'ecl', 'pid', 'eyr', 'hcl', 'iyr', 'hgt', 'byr'}
    return fields <= keys


def count_valid(passwords: list) -> int:
    count = 0
    for password in passwords:
        keys = parse_password(password)
        if isvalid(keys):
            count += 1
    return count


if __name__ == '__main__':
    passwords = extract_passwords('input.txt')
    valid = count_valid(passwords)
    print(valid)
