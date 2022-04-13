# answer 전역변수 지정
answer = 0  

# L : Level로 트리구조에서 층, S : Sum
def dfs(L, S, numbers, target):
    global answer
    N = len(numbers)
    # Level이 numbers의 길이만큼 들어왔고 합이 target과 일치하면 return 카운트 += 1
    if L == N : 
        if target == S:
            answer += 1
            return
    # Level이 numbers의 길이만큼 들어올때까지 합구하면서 아래로 탐색
    else:
        dfs(L+1, S + numbers[L], numbers, target)
        dfs(L+1, S - numbers[L], numbers, target)


def solution(numbers, target):
    global answer
    dfs(0, 0, numbers, target)    
    
    return answer