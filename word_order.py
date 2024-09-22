from collections import OrderedDict

word_count = OrderedDict()

n = int(input())

for _ in range(n):
    word = input().strip()
    if word in word_count:
        word_count[word] +=1
    else:
        word_count[word] = 1
        
print(len(word_count))

print(' '.join(map(str, word_count.values())))