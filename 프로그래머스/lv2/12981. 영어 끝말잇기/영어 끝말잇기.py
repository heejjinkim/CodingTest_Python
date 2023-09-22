def solution(n, words):
    
    for idx in range(1, len(words)):
        if words[idx][0]!=words[idx-1][-1] or len(words[idx])==1:
            return [idx%n+1,idx//n+1]
        
        for j in range(idx): #if words[idx] in words[:idx]:
            if words[j]==words[idx]:
                return [idx%n+1, idx//n+1]

    return [0,0]