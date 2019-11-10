

def compute_freq(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

def generate_pal_perm(s):
    print("===", s, "===")
    d = compute_freq(s)
    found = None
    for k,v in d.items():
        if v % 2 != 0:
            if found:
                print("Palindrome not possible.")
                return None
            else:
                found = k
    if found:
        d[found] -= 1
    
    for k, v in d.items():
        nv = v/2
        d[k] = nv
        if nv == 0:
            del d[k]
    print_palindromes(d, found, len(s)/2)

def print_pal(perm, found):
    if not found:
        found = ''
    perm = "".join(perm)
    print(perm + found + perm[::-1])

def print_palindromes(d, found, L, perm=None, pos=0):
    if not perm:
        perm = [' '] * L
    if pos >= L:
        print_pal(perm, found)

    for k, v in d.items():
        if v == 0:
            continue;
        perm[pos] = k
        nd = d.copy()
        nd[k] -= 1
        print_palindromes(nd, found, L, perm, pos + 1)


def main():
    generate_pal_perm("ppaa")
    generate_pal_perm("ppaap")
    generate_pal_perm("abaaba")

if __name__ == '__main__':
    main()
