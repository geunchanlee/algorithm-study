import sys

sys.setrecursionlimit(500000)


def quickSort(a, l, r):
    if r > l:
        i = partition(a, l, r)
        quickSort(a, l, i - 1)
        quickSort(a, i + 1, r)


def partition(a, l, r):
    v = a[r]
    i = l - 1
    j = r
    while True:
        i += 1
        while a[i] < v:
            i += 1
        j -= 1
        while a[j] >= v:
            j -= 1
        if i >= j:
            break
        a[i], a[j] = a[j], a[i]
    a[i], a[r] = a[r], a[i]
    return i


def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if a[i] > a[i + 1]:
            isSorted = False
        if not isSorted:
            break
    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")


import random, time

N = 100000
a = []
a.append(-1)
for i in range(N):
    a.append(random.randint(1, N))
start_time = time.time()
quickSort(a, 1, N)
end_time = time.time() - start_time
print("퀵 정렬의 실행 시간 (N = %d) : %0.3f" % (N, end_time))
checkSort(a, N)
