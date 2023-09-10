def solution(n, m, section):
    start = section[0]
    answer = 1
    
    for num in section:
        end = start + m - 1
        if start <= num and num <= end:
            continue
        answer += 1
        start = num
    
    return answer