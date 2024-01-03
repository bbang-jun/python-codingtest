def solution(answers):
    persons = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    score = [0]*3
    result = []
    
    for i, answer in enumerate(answers):
        for j, person in enumerate(persons):
            if answer == person[i % len(person)]:
                score[j] += 1
    
    max_score = max(score)
    
    for i in range(len(persons)):
        if max_score == score[i]:
            result.append(i+1)
    
    result.sort()
    return result