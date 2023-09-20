def solution(s):
    ar = sorted([int(n) for n in s.split(" ")]) #list(map(int, s.split()))
    return str(ar[0])+" "+str(ar[-1]) #min, max 사용 가능