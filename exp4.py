def xor(cs, g):
    return [(cs[i] ^ g[i]) for i in range(len(g))]

def crc(data, g):
    cs = data[:len(g)]
    for i in range(len(data) - len(g) + 1):
        if cs[0] == 1:
            cs = xor(cs, g)
        cs = cs[1:] + [data[i + len(g)] if i + len(g) < len(data) else 0]
    return cs[:-1]

def main():
    data = list(map(int, input("Enter the data bits: ").split()))
    g = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
    data += [0] * (len(g) - 1)
    checksum = crc(data, g)
    codeword = data[:len(data) - len(g) + 1] + checksum
    print("Final Codeword:", codeword)

    if int(input("Test Error detection 0(yes) 1(no) ?: ")) == 0:
        pos = int(input("Enter position where error is to be inserted: "))
        codeword[pos] ^= 1
        print("Erroneous data:", codeword)

    if any(crc(codeword, g)):
        print("ERROR in Received Codeword")
    else:
        print("No Error in Received Codeword")

if __name__ == "__main__":
    main()