def solution(s):
    stack=[]
    
    for w in s:
        if w=='(':
            stack.append(w)
        else:
            if stack:
                stack.pop()
            else:
                return False
    
    if stack:
        return False
    
    return True