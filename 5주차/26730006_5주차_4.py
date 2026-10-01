N = int(input())
numbers = []

for _ in range(N):
    numbers.append(int(input()))

avg = sum(numbers) // N

print(avg)
