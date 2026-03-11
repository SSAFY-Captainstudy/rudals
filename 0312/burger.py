def recur(level, arr) :
    if level == N :
        cnt = 0
        for i in range (-X, 0):
           if arr[i] == "p":
               cnt += 1
        print(cnt)
        return

    recur(level+1, ["b"]+arr+["p"]+arr+["b"])


N, X = map(int, input().split())
first = ["p"]
recur(0,first)

# 메모리 초과 발생 !
# 이런 경우에 어떻게 메모리를 줄이는지 알고싶습니다