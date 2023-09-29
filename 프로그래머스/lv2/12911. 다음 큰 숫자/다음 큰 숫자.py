def solution(n):
    bn=bin(n)[2:]
    
    for num in range(n+1,1000001):
        if bn.count('1')==bin(num)[2:].count('1'):
            return num