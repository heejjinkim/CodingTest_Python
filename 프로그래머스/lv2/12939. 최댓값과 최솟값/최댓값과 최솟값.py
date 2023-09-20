def solution(s):
    ar = sorted([int(n) for n in s.split(" ")])
    return str(ar[0])+" "+str(ar[-1])