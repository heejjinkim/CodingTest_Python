def solution(s, n):
    ans=""
    
    for c in s:
        if c==' ':
            ans+=c
        elif c.islower():
            ans+=chr((ord(c)+n-ord('a'))%26 +ord('a'))
        elif c.isupper():
            ans+=chr((ord(c)+n-ord('A'))%26 +ord('A'))
            
    return ans