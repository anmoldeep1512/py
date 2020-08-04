
def bsearch(K, N, x):
    l = 1
    u = N
    while u >= l:
        m = (l+u)//2
        if x == K[m]:
            print("Success")
            return m
        elif x < K[m]:
            u = m - 1
        else:
            l = m + 1
    return -1


A = [1,4,6,9,11,32]

print(bsearch(A, len(A), 9))