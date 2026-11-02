# Savol: Ikki xonali son raqamlari yig'indisi juft yoki toqligini aniqlang.
# Yechim: O'nlik va birlik raqamini qo'shib, yig'indini 2 ga bo'ling.
n = int(input("Ikki xonali son: "))
n = abs(n)
onlik = n // 10
birlik = n % 10
yigindi = onlik + birlik
if yigindi % 2 == 0:
    print("Yig'indi juft")
else:
    print("Yig'indi toq")
