# Savol: Uchta sonning eng katta ikkitasini qo'shing.
# Yechim: Eng kichik sonni topib, qolgan ikkitasini qo'shing.
a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))
if a <= b and a <= c:
    print("Yig'indi:", b + c)
elif b <= a and b <= c:
    print("Yig'indi:", a + c)
else:
    print("Yig'indi:", a + b)
