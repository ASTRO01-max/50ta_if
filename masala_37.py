# Savol: Fil bir yurishda bir katakdan ikkinchisiga o'ta olishini tekshiring.
# Yechim: Fil qator va ustun bo'yicha teng masofaga yuradi.
x1 = int(input("X1 (1-8): "))
y1 = int(input("Y1 (1-8): "))
x2 = int(input("X2 (1-8): "))
y2 = int(input("Y2 (1-8): "))
if abs(x1 - x2) == abs(y1 - y2) and (x1 != x2 or y1 != y2):
    print("Fil o'ta oladi")
else:
    print("Fil o'ta olmaydi")
