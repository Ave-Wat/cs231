def diffie_hellman(output, g, p):
    for i in range(100):
        exp = g**i
        if exp%p == output:
            return i
            break

def rsa():
    for i in range(2, 4661):
        if (4661 % i) == 0:
            print("p = ", i)
            print("q = ", (4661/i), "\n")

    sol = 0
    d = 0
    while sol != 1:
        d += 1
        sol = (31 * d) % (78 * 58)
    print(d)


def main():
    g = 17
    p = 61
    A = 5
    B = 46
    a = diffie_hellman(A, g, p)
    b = diffie_hellman(B, g, p)
    print("axb = " + str(a*b))

if __name__ == '__main__':
    main()
