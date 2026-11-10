n = 22  

for i in range(1, n + 6):
    print(i, end=" ")
print()

m = int(input())
k = int(input())

if m <= k:
    for i in range(m, k + 1):
        print(i, end=" ")
else:
    for i in range(m, k - 1, -1):
        print(i, end=" ")
print()

сума = 0
while True:
    число = float(input())
    if число == 0:
        break
    сума += music_сума = сума + число
    сума += число
print(сума)

рядок4 = input()
print(рядок4[::2])

рядок5 = input()
print(рядок5.count('*'))

рядок6 = input()
print(рядок6[::-1])

рядок7 = input()
print(рядок7[::7])
