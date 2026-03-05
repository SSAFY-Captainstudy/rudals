import sys

minn = 10^9

def cook(idx,sour,bitter,count) :
    global minn
    if idx == N :
        if count > 0 :
            num = abs(sour-bitter)
            if minn > num :
                minn = num
        return

    # 현재 인덱스의 재료 넣었을 때
    cook(idx+1, sour*ingredients[idx][0], bitter+ingredients[idx][1], count+1)
    # 현재 인덱스의 재료를 넣지 않았을 때
    cook(idx+1, sour, bitter, count)



N = int(sys.stdin.readline())
ingredients = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cook(0, 1, 0 ,0)
print(minn)