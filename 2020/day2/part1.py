def isvalid(s):
    policy, password = s.split(':')
    bounds, letter = policy.split()
    l_bound, u_bound = map(int, bounds.split('-'))
    occurences = password.count(letter)
    if l_bound <= occurences <= u_bound:
        return True
    return False


count = 0
with open('input.txt', 'r') as file:
    for line in file.readlines():
        if isvalid(line):
            count += 1
print(count)
