import sys

input = sys.stdin.readline

n = int(input())

alist=list(map(int, input().split()))
blist=list(map(int, input().split()))

alist.sort()
total = 0

for i in range(n):
  a = alist[i]
  b = blist.pop(blist.index(max(blist)))
  total += a*b

print(total)