# N = 5
# road = [2,3,4,5]
# price = [5,2,3,1,1]
N = 4
road = [2,3,1]
price = [5,2,4,1]
price.pop()
answer = 0
low = min(price)
pivot = price[0]
for i in range(N-1):
    if pivot > price[i]:
        pivot = price[i]
    if price[i] != low:
        answer += road[i]*pivot
        road[i] = 0
    elif pivot == low:
        answer += sum(road)*low
        break           
print(answer)