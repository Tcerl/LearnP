n =  int(input())
a = []
for i in range(n):
    a.append(int(input()))
is_increase = all(a[i] > a[i-1] for i in range(1, n))
is_decrease = all(a[i] < a[i-1] for i in range(1, n))
if is_increase or is_decrease:
    print("YES")
else:
    print("NO")