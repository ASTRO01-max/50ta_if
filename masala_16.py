# Savol: Uch xonali sonning birinchi va oxirgi raqami tengligini tekshiring.
# Yechim: Yuzlik raqamini birlik raqami bilan solishtiring.
n = int(input("Uch xonali son: "))
n = abs(n)
if n // 100 == n % 10:
    print("Teng")
else:
    print("Teng emas")
