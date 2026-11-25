# 1
suma = 0

for i in range(2, 101):
    if i % 2 == 0:
        suma += i

print(suma)
suma = 0
# 2
for i in range(2, 101):
        suma += i*i

print(suma)
suma = 0
# 3
for i in range(1, 64):
    suma += 2**i

print(suma)
suma = 0
# 4
a = 432543
b = 3124


for i in range(a, b + 1):
    if i % 2 == 1:
        suma += i

print(suma)
suma = 0