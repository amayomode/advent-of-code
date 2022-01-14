from parse_input import parseInput


def parse_subpackets(packet, start, ver_sums):
    if all(i == "0" for i in packet[start:]):
        return ver_sums

    ver_sums += int(packet[start: start + 3], 2)
    t_Id = int(packet[start + 3: start + 6], 2)

    if t_Id == 4:
        start += 6
        while True:
            bits = packet[start: start + 5]
            if bits[0] == "0":
                break
            start += 5
        start += 5
        return parse_subpackets(packet, start, ver_sums)
    else:
        start += 6
        l_type_id = packet[start]
        if l_type_id == "0":
            start += 16
            return parse_subpackets(packet, start, ver_sums)
        else:
            start += 12
            return parse_subpackets(packet, start, ver_sums)


if __name__ == '__main__':
    packet = parseInput("input.txt")
    print(parse_subpackets(packet, start=0, ver_sums=0))
