def mod_exp(base, exp, mod):
    # Efficient modular exponentiation function
    result = 1
    base = base % mod
    while exp > 0:
        if (exp % 2) == 1:  # If exp is odd, multiply base with result
            result = (result * base) % mod
        exp = exp >> 1  # exp = exp // 2
        base = (base * base) % mod  # Square the base
    return result

def gcd(a, b):
    # Function to calculate gcd
    while b != 0:
        a, b = b, a % b
    return a

def find_d(e, Z):
    # Calculate d such that (d * e) % Z = 1
    d = 1
    while (e * d) % Z != 1:
        d += 1
    return d

# Main RSA logic
def main():
    p = int(input("Enter a prime number p: "))
    q = int(input("Enter a prime number q: "))
    n = p * q
    Z = (p - 1) * (q - 1)

    print(f"p = {p}, q = {q}, n = {n}, Z = {Z}")

    e = int(input("Enter an integer e (1 < e < Z) and coprime to Z: "))
    while gcd(e, Z) != 1:
        print("e is not coprime with Z. Choose another e.")
        e = int(input("Enter an integer e (1 < e < Z): "))

    d = find_d(e, Z)

    print(f"Public key (e, n): ({e}, {n})")
    print(f"Private key (d, n): ({d}, {n})")

    message = input("Enter message to encrypt: ")
    pt = [ord(char) for char in message]

    # Encryption
    ct = [mod_exp(char, e, n) for char in pt]
    print("\nCipher Text:")
    print(ct)

    # Decryption
    decrypted_pt = [mod_exp(char, d, n) for char in ct]
    decrypted_message = ''.join([chr(char) for char in decrypted_pt])
    print("\nDecrypted Text:")
    print(decrypted_message)

if __name__ == "__main__":
    main()