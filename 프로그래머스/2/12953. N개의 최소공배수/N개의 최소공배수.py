def solution(arr):
    pre_lcm = lcm = max(arr)
    
    while arr:
        temp_max = max(arr) #현재 arr 에서의 max 값
        if lcm%temp_max!=0:
            lcm+=pre_lcm
        else:
            arr.remove(temp_max)
            pre_lcm=lcm # 이전까지의 최소 공배수 업데이트
        
    return lcm