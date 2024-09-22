from collections import defaultdict

# Đọc số lượng phần tử của hai nhóm
n, m = map(int, input().split())

# Khởi tạo defaultdict để lưu trữ các vị trí xuất hiện của từ trong nhóm A
group_a = defaultdict(list)

# Đọc các từ trong nhóm A và lưu trữ vị trí của chúng
for i in range(1, n + 1):
    word = input()
    group_a[word].append(i)

# Đọc các từ trong nhóm B và kiểm tra sự xuất hiện trong nhóm A
for _ in range(m):
    word = input()
    if word in group_a:
        print(' '.join(map(str, group_a[word])))
    else:
        print(-1)
