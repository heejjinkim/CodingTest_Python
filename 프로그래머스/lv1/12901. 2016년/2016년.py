def solution(a, b):
    week={1:"FRI", 2:"SAT", 3:"SUN", 4:"MON", 5:"TUE", 6:"WED", 0:"THU"}
    day=[31,29,31,30,31,30,31,31,30,31,30,31]

    return week.get(sum(day[:a-1],b)%7)