#Radix Sort using counting sort on letters 
def counting_sort_digits(A,letter_num):
    k = 26 #zakres alfabetu uwzgledniamy tylko małe
    C = [0] * k
    B = [0]*len(A)
    for i in range(len(A)):
        C[ord(A[i][letter_num]) - ord('a')] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        C[ord(A[i][letter_num]) - ord('a')] -= 1
        B[C[ord(A[i][letter_num]) - ord('a')]] = A[i]
    return B

def radix_sort(A, k):
    for i in range(k - 1, -1, -1):
        A = counting_sort_digits(A,i)
    return A

T = ["abc","aaa","bbb","abo","kub"]
print(radix_sort(T,3))