# SORTOWANIE WYRAZÓW O TEJ SAMEJ DLUGOSCI   # O(d( n + k))  k-liczba róznych cyfr , d = liczba cyfr w liczbach,
def radixSort1(A, numOfWords, lenOfWord): 
    for i in range(lenOfWord-1, -1, -1):
        for j in range(0, numOfWords):
            currWord = 0
            while currWord + j < numOfWords - 1:
                if(A[currWord][i]  > A[currWord + 1][i]):
                    A[currWord], A[currWord + 1] = A[currWord + 1], A[currWord]
                currWord += 1
    return A

# SORTOWAIE WYRAZOW O ROZNEJ DLUGOSCI

def radix(A, n, d):
    for j in range(1, n):
        while j > 0:
            if A[j][d] < A[j - 1][d]:
                A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1
    return A

def sortstring(A):
    bucket = []
    for i in A:
        while len(i) >= len(bucket):
            bucket.append([])
        bucket[len(i)].append(i)

    for i in range(len(bucket) - 1, 0, -1):
        q = len(bucket[i])
        C = radix(bucket[i], q, i - 1)
        bucket[i - 1] = bucket[i] + bucket[i - 1]
    return C

# SORTOWANIE LICZB
def countingSort(A, x):
    n = len(A)
    output = [0] * n

    count = [0] * 10
    for i in range(0, n):
        index = (A[i] / x)
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (A[i] / x)
        output[count[int(index % 10)] - 1] = A[i]
        count[int(index % 10)] -= 1
        i -= 1

    i = 0
    for i in range(0, len(A)):
        A[i] = output[i]

def radixdlaliczb(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10
    return arr

if __name__ == '__main__':
    A = [5,8,10,15,65,76,33,0,234,78,100,567,34,8]
    print(radixdlaliczb(A))