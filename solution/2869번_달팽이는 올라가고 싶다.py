a, b, v = map(int, input().split())  # a: 낮에 올라가는 길이, b: 밤에 미끄러짐, v: 높이
result = (v - a) // (a - b) # 달팽이가 거의 도착하기 하루 전 or 이틀 전
print(result + 1) if a >= v- (result*(a-b)) else print(result + 2)