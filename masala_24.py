# Savol: Uchta son ichidagi toq sonlar yig'indisini toping.
# Yechim: Har bir son toq bo'lsa, uni yig'indiga qo'shing.
a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
yigindi = 0
if a % 2 != 0:
    yigindi = yigindi + a
if b % 2 != 0:
    yigindi = yigindi + b
if c % 2 != 0:
    yigindi = yigindi + c
print("Yig'indi:", yigindi)
