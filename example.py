# This file contains three arbitrary medium-to-large-sized
# functions with varying numbers of uninitialized
# variables. Each function has a comment above its
# definition explaining how many uninitialized variables
# the function contains and their names.


# has 2 uninitialized variables: i and c
def cgi_decode(self, s):
    hex_values = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
    }

    t = ""
    i: int

    while i < len(s):
        c: str
        if c == '+':
            t += ' '
        elif c == '%':
            digit_high, digit_low = s[i + 1], s[i + 2]
            i += 2
            if digit_high in hex_values and digit_low in hex_values:
                v = hex_values[digit_high] * 16 + hex_values[digit_low]
                t += chr(v)
            else:
                raise ValueError("Invalid encoding")
        else:
            t += c
        i += 1
    return t


# has 3 uninitialized variables:
# isprime, pos, and globaldenominator
def prime_paths(self):
    START_NUM = 1
    END_NUM = 500
    CROAK_SEQ = "PPPPNNPPPNPPNPN"
    assert 0 <= START_NUM < END_NUM
    assert 1 <= len(CROAK_SEQ)

    NUM_JUMPS = len(CROAK_SEQ) - 1
    NUM_TRIALS = 2 ** NUM_JUMPS

    globalnumerator = 0
    isprime: bool

    for i in range(START_NUM, END_NUM + 1):

        for j in range(NUM_TRIALS):

            pos: str
            trialnumerator = 1
            if isprime[pos] == (CROAK_SEQ[0] == 'P'):
                trialnumerator *= 2

            for k in range(NUM_JUMPS):
                if pos <= START_NUM:
                    pos += 1
                elif pos >= END_NUM:
                    pos -= 1
                elif (j >> k) & 1 == 0:
                    pos += 1
                else:
                    pos -= 1

                if isprime[pos] == (CROAK_SEQ[k + 1] == 'P'):
                    trialnumerator *= 2
            globalnumerator += trialnumerator

    globaldenominator: int
    return str("result")


# has 0 uninitialized variables
def solve_sudoku(puzzlestr):
    assert len(puzzlestr) == 81
    state = [int(c) for c in puzzlestr]
    colfree = [set(range(1, 10)) for i in range(9)]
    rowfree = [set(range(1, 10)) for i in range(9)]
    boxfree = [set(range(1, 10)) for i in range(9)]
    for y in range(9):
        for x in range(9):
            d = state[y * 9 + x]
            if d != 0:
                colfree[x].remove(d)
                rowfree[y].remove(d)
                boxfree[y // 3 * 3 + x // 3].remove(d)

    def recurse(i):
        if i == 81:
            return True
        elif state[i] != 0:
            return recurse(i + 1)
        else:
            x = i % 9
            y = i // 9
            j = y // 3 * 3 + x // 3
            candidates = colfree[x].intersection(rowfree[y], boxfree[j])
            for d in candidates:
                state[i] = d
                colfree[x].remove(d)
                rowfree[y].remove(d)
                boxfree[j].remove(d)
                if recurse(i + 1):
                    return True

                colfree[x].add(d)
                rowfree[y].add(d)
                boxfree[j].add(d)
            state[i] = 0
            return False

    if not recurse(0):
        raise AssertionError("Unsolvable")
    return state
