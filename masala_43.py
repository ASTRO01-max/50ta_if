# Savol: Kvadrat tenglama nechta haqiqiy ildizga ega ekanini toping.
# Yechim: D = B*B - 4*A*C; D musbat, nol yoki manfiyligini tekshiring.
a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))
d = b * b - 4 * a * c
if d > 0:
    print("2 ta ildiz")
elif d == 0:
    print("1 ta ildiz")
else:
    print("Haqiqiy ildizi yo'q")
