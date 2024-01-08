def solution(dirs):
    
    answer = set()
    cur_x, cur_y = 5, 5

    for i, dir in enumerate(dirs):
        nx, ny = cur_x, cur_y
        if dir == 'U':
            ny +=1
        elif dir == 'D':
            ny -=1
        elif dir == 'R':
            nx +=1
        elif dir == 'L':
            nx -=1
        
        # 다음 위치가 좌표를 넘어가는지 체크
        if nx > 10 or nx < 0 or ny > 10 or ny < 0:
            continue
        
        answer.add((cur_x, cur_y, nx, ny))
        answer.add((nx, ny, cur_x, cur_y))
        cur_x, cur_y = nx, ny
        
    return len(answer) / 2