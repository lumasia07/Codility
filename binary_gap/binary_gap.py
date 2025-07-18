"""Binary Gap"""

def solution(N):
    binary = bin(N)[2:]
    max_gap = 0
    current_gap = 0
    counting = False

    for bit in binary:
        if bit == '1':
            if counting:
                max_gap = max(max_gap, current_gap)
            counting = True
            current_gap = 0
        elif counting:
            current_gap += 1
    return max_gap
