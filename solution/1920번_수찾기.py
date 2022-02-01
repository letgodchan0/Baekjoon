N = int(input())
array = list(map(int, input().split()))
array.sort()
M = int(input())
check = list(map(int, input().split()))

def find(array, number, start, end):
    if start > end:
        return 0
    mid = (start+end) // 2
    if array[mid] == number:
        return 1
    elif array[mid] > number:
        return find(array, number, start, mid-1)
    else :
        return find(array, number, mid+1, end)
for number in check:
    print(find(array, number, 0, N - 1))