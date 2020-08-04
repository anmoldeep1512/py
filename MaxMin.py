
def maxmin(a, i, j):
    if i == j:
        maxi = a[i]
        mini = a[i]
        return mini, maxi
    elif i == j - 1:
        if a[i] < a[j]:
            maxi = a[j]
            mini = a[i]
        else:
            maxi = a[i]
            mini = a[j]
        return mini, maxi
    else:
        mid = int((i+j)/2)
        x = maxmin(a, i, mid)
        y = maxmin(a, mid + 1, j)
        if x[1] < y[1]:
            maxi = y[1]
        else:
            maxi = x[1]
        if x[0] > y[0]:
            mini = y[0]
        else:
            mini = x[0]
        return mini, maxi


A = [19, 2, 44, 4, 22, 2, 6, 5, 1]
print(maxmin(A, 0, len(A)-1))



