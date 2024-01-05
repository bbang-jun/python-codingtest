def solution(num_list):
    answer = [0] * len(num_list)
    for i, num in enumerate(num_list):
        answer[-i-1] = num
    return answer