# Savol: Ot bir yurishda bir katakdan ikkinchisiga o'ta olishini tekshiring.
# Yechim: Ot 2 katak bir tomonga, 1 katak boshqa tomonga yuradi.
x1 = int(input("X1 (1-8): "))
y1 = int(input("Y1 (1-8): "))
x2 = int(input("X2 (1-8): "))
y2 = int(input("Y2 (1-8): "))
x_farq = abs(x1 - x2)
y_farq = abs(y1 - y2)
if (x_farq == 1 and y_farq == 2) or (x_farq == 2 and y_farq == 1):
    print("Ot o'ta oladi")
else:
    print("Ot o'ta olmaydi")
