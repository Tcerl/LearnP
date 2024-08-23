n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

frequency = {}

for num in a:
    if num in frequency:
        frequency +=1
    else:
        frequency = 1

unique_numbers = sorted(frequency.keys())

result = []
for num in unique_numbers:
    result.append(f"{num} - frequency[num]")

print("".join(result) + "; ")
