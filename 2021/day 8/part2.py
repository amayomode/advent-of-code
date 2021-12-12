from decode import decode_output

with open("input.txt", "r") as f:
    sum = 0
    for line in f.readlines():
        signal_patterns, output = line.split('|')
        output_value = decode_output(signal_patterns, output)
        sum += output_value
    print(sum)
