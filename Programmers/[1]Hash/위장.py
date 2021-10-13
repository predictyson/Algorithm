def solution(clothes):
    answer = 1
    closet = {}
    cate = 0
    for name, cate in clothes :
        if cate in closet :
            closet[cate] += 1
        else :
            closet[cate] = 1
    for key, value in closet.items() : 
        answer *= (value+1)
    return answer-1