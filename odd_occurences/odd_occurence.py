"""Odd occurence in array"""

def solution(A):
    unpaired = 0
    for number in A:
        unpaired ^= number
    return unpaired
