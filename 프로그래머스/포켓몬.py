
def solution(nums):
    answer = 0

    monster = list(set(nums))

    for x in monster:
        if answer < len(nums )/ /2:
            answer += 1

    return answer