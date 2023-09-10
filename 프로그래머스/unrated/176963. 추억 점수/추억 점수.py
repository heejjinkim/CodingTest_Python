def solution(name, yearning, photo):
    answer = []
    
    for x in photo:
        sum = 0
        for y in x:
            if y in name:
                idx = name.index(y)
                sum += yearning[idx]
                
        answer.append(sum)
    
    return answer