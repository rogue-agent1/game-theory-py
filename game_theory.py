#!/usr/bin/env python3
"""Nash equilibrium — support enumeration for 2-player normal-form games."""
from itertools import combinations

def solve_2x2(A, B):
    """Find mixed Nash for 2x2 game. A[i][j] = row player payoff."""
    m, n = len(A), len(A[0])
    results = []
    # Check pure strategy NE
    for i in range(m):
        for j in range(n):
            row_best = max(A[r][j] for r in range(m))
            col_best = max(B[i][c] for c in range(n))
            if A[i][j] == row_best and B[i][j] == col_best:
                p = [0]*m; q = [0]*n; p[i] = 1; q[j] = 1
                results.append((p, q, A[i][j], B[i][j]))
    # Mixed strategy for 2x2
    if m == 2 and n == 2:
        denom_q = (A[0][0]-A[0][1]-A[1][0]+A[1][1])
        denom_p = (B[0][0]-B[0][1]-B[1][0]+B[1][1])
        if abs(denom_q) > 1e-10 and abs(denom_p) > 1e-10:
            q = (A[1][1]-A[1][0]) / denom_q
            p = (B[1][1]-B[0][1]) / denom_p
            if 0 < p < 1 and 0 < q < 1:
                ev1 = p*q*A[0][0]+p*(1-q)*A[0][1]+(1-p)*q*A[1][0]+(1-p)*(1-q)*A[1][1]
                ev2 = p*q*B[0][0]+p*(1-q)*B[0][1]+(1-p)*q*B[1][0]+(1-p)*(1-q)*B[1][1]
                results.append(([p,1-p],[q,1-q],ev1,ev2))
    return results

def main():
    # Prisoner's dilemma
    A = [[-1,-3],[0,-2]]; B = [[-1,0],[-3,-2]]
    eqs = solve_2x2(A, B)
    for p,q,v1,v2 in eqs: print(f"NE: p={p}, q={q}, payoffs=({v1},{v2})")

if __name__ == "__main__": main()
