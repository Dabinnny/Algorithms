from collections import deque

def solution(people, limit):
    people.sort()  
    boat = 0
    p = deque(people)
    
    while p:
        if len(p) >= 2 :
            if p[0] + p[-1] <= limit:  
                p.pop()
                p.popleft()
                boat += 1
            elif p[0] + p[-1] > limit:
                p.pop()
                boat += 1
        else :
            if p[0] <= limit:
                p.pop()
                boat += 1
    return boat

'''사람들의 무게를 오름차순으로 정렬한다.
사람들의 리스트를 deque형식으로 만들어 무게가 제일 많이 나가는 사람을 고른뒤 제일 가벼운 사람과 더해서 limit 이하인지 확인다.
만약 무게가 limit 이하라면 앞에 하나, 뒤에 하나 pop하고 두 사람을 보트에 태운다는 의미에서 boat를 하나 증가시킨다.
그래도 만약 앞 뒤 사람의 합이 limit를 초과한다면 보트에 둘이 담을 수 없기에 제일 무게가 많이 나가는 사람을 pop 한다.(탐욕:무거운 사람을 태워야 남은 가벼운 사람들이 보트에 2명씩 타서 보트 수를 줄일 가능성이 높아지기 때문이다.) 보트는 당연히 하나 더 증가.
가장 무거운 사람을 태우되 남은 1자리를 가벼운 사람부터 차례대로 고려한다. 남은 사람들 중 가장 가벼운데 무게가 초과됬다는 말은 두번째로 가벼운 사람 역시 초과될 것이라는 뜻. 더 이상 고려할 필요가 없게 된다. 초과되면 무거운 사람만 보트에 한명 태우고 나머지 형식도 반복해서 최대한 무거운+가벼운 사람의 조합을 사용해 보트를 최소화 한다.'''