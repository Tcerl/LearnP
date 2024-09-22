from collections import OrderedDict

ordered_dict = OrderedDict()

n = int(input())

for _ in range(n):
    item, space, price = input().rpartition(' ')
    price = int(price)
    
    if item in ordered_dict:
        ordered_dict[item] += price
    else:
        ordered_dict[item] = price
        

for item, total_price in ordered_dict.items():
    print(item, total_price)