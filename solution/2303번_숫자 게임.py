n = int(input())  

lst = []        
for _ in range(n):
  check = list(map(int, input().split())) 
  res = 0 
  for i in range(5):
    for j in range(i + 1, 5):
      for k in range(j + 1, 5):
        num = (check[i] + check[j] + check[k]) % 10 
        if num >= res: res=num 
  lst.append(res)

for i in range(n - 1, -1, -1): 
  if lst[i] == max(lst): 
    print(i + 1)
    break