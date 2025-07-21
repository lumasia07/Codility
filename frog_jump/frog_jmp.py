"""Shortest distance for frog"""

def solution(X, Y, D):
    distance = Y - X
    jumps = (distance + D - 1) // D
    return jumps
