from parse_input import parseInput
from math import prod

# had to rethink the approach here


def parse_subpackets(packet, start):
    t_Id = int(packet[start + 3: start + 6], 2)

    operations = {
        0: sum,
        1: prod,
        2: min,
        3: max,
        5: lambda x: int(x[0] > x[1]),
        6: lambda x: int(x[0] < x[1]),
        7: lambda x: int(x[0] == x[1])
    }

    if t_Id == 4:
        start += 6
        l_value = ""
        while True:
            bits = packet[start: start + 5]
            l_value += bits[1:]
            if bits[0] == "0":
                break
            start += 5
        start += 5
        return start, int(l_value, 2)

    else:
        start += 6
        l_type_id = packet[start]
        values = []
        if l_type_id == "0":
            len_sub_pkts = int(packet[start+1: start+16], 2)
            start += 16
            end = start + len_sub_pkts
            while start < end:
                start, res = parse_subpackets(packet, start)
                values.append(res)

        else:
            num_sub_pkts = int(packet[start+1: start + 12], 2)
            start += 12
            for _ in range(num_sub_pkts):
                start, res = parse_subpackets(packet, start)
                values.append(res)

    return start, operations[t_Id](values)


if __name__ == '__main__':
    packet = parseInput("input.txt")
    print(parse_subpackets(packet, start=0)[1])
