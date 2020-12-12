def two_records(deficit, record):
    for num in record:
        complement = deficit-num
        if complement in record:
            return num*complement
    return None


def three_records(record):
    for i, n in enumerate(record):
        deficit = 2020 - record[i]
        ans = two_records(deficit, record[0:i]+record[i:])
        if ans:
            return record[i] * ans
    return None


with open('input.txt', 'r') as file:
    record = [int(num) for num in file.readlines()]
    print(three_records(record))
