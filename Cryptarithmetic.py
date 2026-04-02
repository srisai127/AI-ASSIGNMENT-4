# Cryptarithmetic CSP (Fig 5.2a)

from itertools import permutations

letters = ['S','E','N','D','M','O','R','Y']

for perm in permutations(range(10), len(letters)):
    S,E,N,D,M,O,R,Y = perm

    # Leading digit constraint
    if S == 0 or M == 0:
        continue

    SEND = 1000*S + 100*E + 10*N + D
    MORE = 1000*M + 100*O + 10*R + E
    MONEY = 10000*M + 1000*O + 100*N + 10*E + Y

    if SEND + MORE == MONEY:
        print("Solution Found:\n")
        print(f"S={S}, E={E}, N={N}, D={D}, M={M}, O={O}, R={R}, Y={Y}")
        print(f"\n{SEND} + {MORE} = {MONEY}")
        break
