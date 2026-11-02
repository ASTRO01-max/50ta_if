# Savol: Olti xonali son omadli, ya'ni ikki yarmi raqamlari yig'indisi tengligini aniqlang.
# Yechim: Dastlabki va oxirgi uch raqam yig'indilarini toping.
n = int(input("Olti xonali son: "))
n = abs(n)
a = n // 100000
b = n // 10000 % 10
c = n // 1000 % 10
d = n // 100 % 10
e = n // 10 % 10
f = n % 10
if a + b + c == d + e + f:
    print("Omadli son")
else:
    print("Omadli son emas")
