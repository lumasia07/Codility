"""Cyclic Rotation"""

def solution(A, K):
    N = len(A)
    if N == 0:
        return A
    K = K % N
    return A[-K:] + A[:-K]
