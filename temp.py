def solution(N, A):
    # write your code in Python 2.7
    ctr = [0] * N
    lenA = len(A)

    currMax = 0
    finalMax = 0

    for i in range(lenA):
        if A[i] >= 1 and  A[i] <= N:
            ctr[A[i] -1] += 1
            if currMax < ctr[A[i] -1]:
                currMax = ctr[A[i] -1]
        else:
            finalMax += currMax
            ctr = [0] * N
            currMax = 0

    for j in range(N):
        ctr[j] += finalMax

    return ctr


print solution(5, [3, 4, 4, 6, 1, 4, 4])
