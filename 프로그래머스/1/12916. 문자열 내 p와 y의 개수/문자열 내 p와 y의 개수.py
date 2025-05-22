def solution(s):
    answer = True
    a, b = 0, 0
    for i in(s):
        if i == 'p' or i == 'P':
            a += 1
        elif i == 'y' or i =='Y':
            b += 1
    if a == b:
        answer = True
    elif a != b:
        answer = False
    return answer