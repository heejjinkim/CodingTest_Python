def solution(s):
    ans=s[0].upper()
    for i in range(1,len(s)):
        if s[i-1]==" ":
            ans+=s[i].upper()
        else:
            ans+=s[i].lower()
            
    return ans 
#' '.join([word.capitalize() for word in s.split(" ")])
