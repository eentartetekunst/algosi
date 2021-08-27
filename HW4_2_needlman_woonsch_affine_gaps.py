seq1 = input('entar seq 1: ')
seq2 = input('enter seq 2: ')
match = 5
mismatch = -4
d = 10
e = 0.5

def build_matrix(matrix, rows, cols):
    for _ in range(rows):
        line = [0] * cols
        matrix.append(line)

def match_check(seq1, seq2):
    if seq1 == seq2:
        return match
    else:
        return mismatch

n = len(seq1)
m = len(seq2)
A, B, S, path = [], [], [], []
build_matrix(A, n, m)
build_matrix(B, n, m)
build_matrix(S, n+1, m+1)
build_matrix(path, n+1, m+1)

for i in range(n):
    S[i+1][0] = -d - e*i
    B[i][0] = S[i+1][0]-d
for j in range(m):
    S[0][j+1] = -d - e*j
    A[0][j] = S[0][j+1]-d

for i in range(n): # cols
    for j in range(m): # rows
        S[i+1][j+1] = max(A[i][j], B[i][j], S[i][j] + match_check(seq1[i], seq2[j]))

        if A[i][j] > B[i][j] and A[i][j] > match_check(seq1[i], seq2[j]):
            path[i+1][j+1] = 'up'
        elif B[i][j] > A[i][j] and B[i][j] > match_check(seq1[i], seq2[j]):
            path[i+1][j+1] = 'left'
        else:
            path[i+1][j+1] = 'diag'

        if i != n-1: # кол-ву столбцов - 1
            A[i+1][j] = max(A[i][j]-e, S[i+1][j+1]-d)
        if j != m-1:
            B[i][j+1] = max(B[i][j]-e, S[i+1][j+1]-d)


check = [n, m]
up_al, down_al = '', ''

for i in range(n, 0, -1):
    for j in range(m, 0, -1):
        if i == check[0] and j == check[1]:
            if path[i][j] == 'diag':
                if i == 1 and j != 1:
                    down_al += seq2[j-1]
                    up_al += '-'
                    check = [i, j-1]
                elif i != 1 and j == 1:
                    down_al += '-'
                    up_al += seq1[i-1]
                    check = [i-1, j]
                else:
                    down_al += seq2[j-1]
                    up_al += seq1[i-1]
                    check = [i-1, j-1]
            elif path[i][j] == 'up':
                down_al += '-'
                up_al += seq1[i-1]
                check = [i-1, j]
            elif path[i][j] == 'left':
                down_al += seq2[j-1]
                up_al += '-'
                check = [i, j-1]
        if i == 1 and j == 1:
            break


align_up = up_al[::1]
align_down = down_al[::1]

print(align_up)
print(align_down)

print('Score: ', S[-1][-1])
#  ATGAGTCTCTCTGATAAGGACAAGGCTGCTGTGAAAGCCCTATGG
#  CTGTCTCCTGCCGACAAGACCAACGTCAAGGCCGCCTGGGGTAAG
