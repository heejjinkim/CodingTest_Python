import math

def solution(brown, yellow):
    all=brown+yellow
    width=3
    
    while True:
        height=all//width  
        if all%width==0 and width>=height and (width-2)*(height-2)==yellow:
            return [width, height]
        width+=1