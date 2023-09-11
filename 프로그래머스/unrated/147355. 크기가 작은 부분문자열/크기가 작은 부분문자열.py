def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        for j in range(len(p)):
            if t[i+j] < p[j]:
                answer += 1
                break
            elif t[i+j] == p[j]:
                if j == len(p)-1:
                    answer += 1
                    break
                continue
            else:
                break

    return answer