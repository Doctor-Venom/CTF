import sys


def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)

    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" %
                   (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

def IP(BYTES):
    LEFT, RIGHT = '', ''
    for i, j in enumerate(BYTES):
        if i % 2:
            LEFT += j
        else:
            RIGHT += j
    return LEFT, RIGHT

def Feistel_Function(_64BIT):
    def expansion(X):
        X = ''.join(f'{ord(x):08b}' for x in X)
        EX = ''
        X = [X[0+i:8+i] for i in range(0, len(X), 8)]
        i = 0
        while i < len(X):
            EX += (X[i-1][-1]+X[i]+X[i][0])
            i += 1
        return EX

    def transposition(EX):
        TEX = ''
        for i in [37, 27, 58, 14, 31, 39, 65, 36, 48, 22, 28, 18, 53, 21, 8, 77, 17, 20, 9, 7, 74, 40, 51, 60, 52, 2, 69, 11, 59, 41, 26, 70, 79, 50, 33, 46, 38, 34, 13, 15, 43, 44, 30, 63, 24, 66, 75, 35, 54, 47, 16, 61, 32, 25, 56, 68, 6, 71, 12, 64, 72, 62, 45, 78, 5, 23, 1, 42, 10, 55, 0, 29, 73, 3, 4, 67, 49, 57, 76, 19]:
            TEX += EX[i]
        TEX = ''.join([chr(int(i, 2)) for i in [TEX[0+i:8+i]
                        for i in range(0, len(TEX), 8)]])
        return TEX

    _80BIT = transposition(expansion(_64BIT))
    return _80BIT

def xor(x, y):
    i = 0
    z = ''
    while i < len(x) and i < len(y):
        z += chr(ord(x[i]) ^ ord(y[i]))
        i += 1
    return z

def FP(LEFT, RIGHT):
    RESULT = ''
    i = 0
    while i < len(LEFT):
        RESULT += RIGHT[i]+LEFT[i]
        i += 1
    return RESULT

def encryption(PT):
    LPT, RPT = IP(PT)
    expanded = ''
    for _ in progressbar(range(8192), "Encryption: ", 50):
        RPT_prime = Feistel_Function(RPT)
        expanded += RPT_prime[8:]
        RPT = RPT[:8]
        LPT = xor(LPT, RPT_prime)
        LPT, RPT = RPT, LPT
    CT = FP(LPT, RPT)+expanded
    print(len(CT))
    print('[+] Encryption Completed!')
    return CT



open('CT_part1', 'w').write(encryption(open('flag.txt').read()[:16].strip()))
open('CT_part2', 'w').write(encryption(open('flag.txt').read()[16:].strip()))
