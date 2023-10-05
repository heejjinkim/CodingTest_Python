def solution(n):
    num=2
    temp1, temp2 = 0,1
    while num<=n:
        result=temp1+temp2
        temp1=temp2
        temp2=result
        num+=1
    
    return result%1234567