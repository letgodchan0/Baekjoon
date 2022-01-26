n = int(input())

# 단어 담아주는 리스트
words = []
for _ in range(n):
    word = input()
    if word not in words:
        words.append(word)

# (1) 길이, (2) 단어 순서대로 정렬하기
words = sorted(words, key = lambda x : (len(x), x))
for word in words:
    print(word)