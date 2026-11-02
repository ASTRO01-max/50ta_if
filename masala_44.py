# Savol: Parallelepiped teshikdan o'ta olishini tekshiring.
# Yechim: Qutining har bir yuzini teshik o'lchamlari bilan ikki xil solishtiring.
a = float(input("Quti A: "))
b = float(input("Quti B: "))
c = float(input("Quti C: "))
x = float(input("Teshik X: "))
y = float(input("Teshik Y: "))
if ((a <= x and b <= y) or (a <= y and b <= x)
        or (a <= x and c <= y) or (a <= y and c <= x)
        or (b <= x and c <= y) or (b <= y and c <= x)):
    print("O'ta oladi")
else:
    print("O'ta olmaydi")
