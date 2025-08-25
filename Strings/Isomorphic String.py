def help(s1, s2):
    m = {}
    if len(s1) != len(s2):
        return False

    n = len(s1)
    for i in range(n):
        if s1[i] not in m:
            m[s1[i]] = s2[i]
        elif m[s1[i]] != s2[i]:
            return False
    return True

def isomorphic(s1, s2):
    return help(s1, s2) and help(s2, s1)


if __name__ == "__main__":
    s1 = input()
    s2 = input()

    if isomorphic(s1, s2):
        print("true")
    else:
        print("false")
