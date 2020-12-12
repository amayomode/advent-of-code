def two_entries(record):
    for num in record:
        complement = 2020 - num
        if complement in record:
            return num * complement


with open('input.txt', 'r') as file:
    record = [int(num) for num in file.readlines()]
    print(two_entries(record))
