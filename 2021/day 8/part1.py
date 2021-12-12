with open("input.txt", "r") as f:
    count = 0
    for line in f.readlines():
        signal_patterns, output = line.split('|')
        for value in output.strip().split():
            if len(value) in [2, 4, 3, 7]:
                count += 1
    print(count)
