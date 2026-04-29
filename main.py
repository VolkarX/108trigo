#!/usr/bin/env python3
import sys
import math

def identity_matrix(size):
    matrix = []
    for i in range(size):
        line = []
        for j in range(size):
            if i == j:
                line.append(1.0)
            else:
                line.append(0.0)
        matrix.append(line)
    return matrix

def mat_add(A, B):
    add_matrix = []
    size = len(A)
    for i in range(size):
        line = []
        for j in range(size):
            line.append(A[i][j] + B[i][j])
        add_matrix.append(line)
    return add_matrix

def mat_mul(A, B):
    size = len(A)
    C = []
    for i in range(size):
        C.append([0.0] * size)
    for i in range(size):
        for j in range(size):
            for k in range(size):
                C[i][j] += A[i][k] * B[k][j]
    return C

def mat_div_scalar(A, scalar):
    size = len(A)
    new_matrix = []
    for i in range(size):
        line =[]
        for j in range (size):
            line.append(A[i][j] / scalar)
        new_matrix.append(line)
    return new_matrix

def exp_matrix(M):
    size = len(M)
    S = identity_matrix(size)
    Term = identity_matrix(size)
    for n in range(1, 100):
        Term = mat_mul(Term, M)
        Term = mat_div_scalar(Term, n)
        S = mat_add(S, Term)
    return S

def cos_matrix(M):
    size = len(M)
    S = identity_matrix(size)
    Term = identity_matrix(size)
    M2 = mat_mul(M, M)
    for n in range(1, 100):
        Term = mat_mul(Term, M2)
        Term = mat_div_scalar(Term, -1.0 * (2 * n) * (2 * n - 1))
        S = mat_add(S, Term)
    return S

def sin_matrix(M):
    size = len(M)
    S = [[M[i][j] for j in range(size)] for i in range(size)]
    Term = [[M[i][j] for j in range(size)] for i in range(size)]
    M2 = mat_mul(M, M)
    for n in range(1, 100):
        Term = mat_mul(Term, M2)
        Term = mat_div_scalar(Term, -1.0 * (2 * n + 1) * (2 * n))
        S = mat_add(S, Term)
    return S

def cosh_matrix(M):
    size = len(M)
    S = identity_matrix(size)
    Term = identity_matrix(size)
    M2 = mat_mul(M, M)
    for n in range(1, 100):
        Term = mat_mul(Term, M2)
        Term = mat_div_scalar(Term, (2 * n) * (2 * n - 1))
        S = mat_add(S, Term)
    return S

def sinh_matrix(M):
    size = len(M)
    S = [[M[i][j] for j in range(size)] for i in range(size)]
    Term = [[M[i][j] for j in range(size)] for i in range(size)]
    M2 = mat_mul(M, M)
    for n in range(1, 100):
        Term = mat_mul(Term, M2)
        Term = mat_div_scalar(Term, (2 * n + 1) * (2 * n))
        S = mat_add(S, Term)
    return S

def print_matrix(M):
    for row in M:
        formatted_row = [f"{val + 0.0:.2f}" for val in row]
        print("\t".join(formatted_row))

def main():
    if len(sys.argv) < 3:
        if len(sys.argv) == 2 and sys.argv[1] == "-h":
            print("USAGE\n    ./108trigo fun a0 a1 a2 ...\n")
            print("DESCRIPTION\n    fun function to be applied, among at least \"EXP\", \"COS\", \"SIN\", \"COSH\" and \"SINH\"")
            print("    ai coeficients of the matrix")
            sys.exit(0)
        sys.exit(84)
    func_name = sys.argv[1]
    valid_funcs = {"EXP": exp_matrix, "COS": cos_matrix, "SIN": sin_matrix, "COSH": cosh_matrix, "SINH": sinh_matrix}
    if func_name not in valid_funcs:
        sys.exit(84)
    try:
        coeffs = [float(x) for x in sys.argv[2:]]
    except ValueError:
        sys.exit(84)
    num_coeffs = len(coeffs)
    if num_coeffs == 0:
        sys.exit(84)
    size = int(math.sqrt(num_coeffs))
    if size * size != num_coeffs:
        print("Error: The matrix must be a square matrix.", file=sys.stderr)
        sys.exit(84)
    matrix = []
    index = 0
    for i in range(size):
        row = []
        for j in range(size):
            row.append(coeffs[index])
            index += 1
    matrix.append(row)
    result = valid_funcs[func_name](matrix)
    print_matrix(result)

if __name__ == "__main__":
    main()