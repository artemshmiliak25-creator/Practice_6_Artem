print("=== ЗАВДАННЯ 1: Список від 1 до n ===")
n1 = int(input("Введіть число n: "))
list1 = list(range(1, n1 + 1))
print(list1)
print("-" * 40)

print("\n=== ЗАВДАННЯ 2: Список букв алфавіту ===")
n2 = int(input("Введіть кількість літер n (до 26): "))
alphabet = [chr(97 + i) for i in range(n2)]
print(alphabet)
print("-" * 40)

print("\n=== ЗАВДАННЯ 3: Список кубів чисел ===")
n3 = int(input("Введіть кількість чисел n: "))
cubes = []
for _ in range(n3):
    num = int(input("Введіть ціле число: "))
    cubes.append(num ** 3)
print(cubes)
print("-" * 40)

print("\n=== ЗАВДАННЯ 4: k-та буква з кожного рядка ===")
n4 = int(input("Введіть кількість рядків n: "))
strings4 = []
for _ in range(n4):
    strings4.append(input("Введіть рядок: "))
k = int(input("Введіть номер букви k: "))

result_chars = ""
for s in strings4:
    if len(s) >= k:
        result_chars += s[k - 1]
print(result_chars)
print("-" * 40)

print("\n=== ЗАВДАННЯ 5: Пошук за запитом ===")
n5 = int(input("Введіть кількість рядків n: "))
strings5 = []
for _ in range(n5):
    strings5.append(input("Введіть рядок: "))
query = input("Введіть пошуковий запит: ")

for s in strings5:
    if query in s:
        print(s)
print("-" * 40)

print("\n=== ЗАВДАННЯ 6: Перевірка IP-адреси ===")
ip_input = input("Введіть IP-адресу (4 числа через крапку): ")
parts = ip_input.split('.')

is_valid = True
if len(parts) != 4:
    is_valid = False
else:
    for part in parts:
        if not part.isdigit() or not (0 <= int(part) <= 255):
            is_valid = False
            break

if is_valid:
    print("ТАК (Коректна IP-адреса)")
else:
    print("НІ (Некоректна IP-адреса)")
print("-" * 40)

print("\n=== ЗАВДАННЯ 7: Вираз зі знаком + та сума ===")
numbers_str = input("Введіть натуральні числа через пробіл: ").split()
expression = "+".join(numbers_str)
total_sum = sum(int(x) for x in numbers_str)
print(f"{expression}={total_sum}")
print("=" * 40)
