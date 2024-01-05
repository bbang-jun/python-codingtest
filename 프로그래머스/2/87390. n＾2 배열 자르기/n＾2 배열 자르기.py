def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1):
        answer.append(max(i//n, i%n)+1)
            
    return answer

# def solution(n, left, right):
#     answer = []
#     arr = [[0 for _ in range(n+1)] for _ in range(n+1)]
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             arr[i][j] = i
#             arr[j][i] = i
            
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             answer.append(arr[i][j])
            
#     return answer[left:right+1]