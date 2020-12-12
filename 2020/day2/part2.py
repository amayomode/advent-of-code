def isvalid(s):
    policy, password = s.split(':')
    bounds, letter = policy.split()
    first, second = map(int, bounds.split('-'))
    condition = (password[first] == letter, password[second] == letter)
    if any(condition) and not all(condition):
        return True
    return False


count = 0
with open('input.txt', 'r') as file:
    for line in file.readlines():
        if isvalid(line):
            count += 1
print(count)
