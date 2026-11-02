# Savol: A va B teng bo'lmasa, ikkalasiga yig'indisini; teng bo'lsa, 0 yozing.
# Yechim: Avval yig'indini hisoblang, keyin ikkala qiymatni o'zgartiring.
a = int(input("A = "))
b = int(input("B = "))
if a != b:
    yigindi = a + b
    a = yigindi
    b = yigindi
else:
    a = 0
    b = 0
print("A =", a)
print("B =", b)
