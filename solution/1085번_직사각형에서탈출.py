# 입력받기
x, y, w, h = map(int,input().split())
result = []
# result에 값 추가
result.append(x)
result.append(y)
result.append(w-x)
result.append(h-y)
# 최소값 출력
print(min(result))