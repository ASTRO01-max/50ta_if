# Savol: Tezlik oshishiga qarab jarimani aniqlang: 1-20: $100, 20-40: $200, 40 dan ko'p: $500.
# Yechim: Ruxsat etilgan tezlikni ayirib, oshish miqdorini tekshiring.
v = float(input("Tezlik (km/soat): "))
v_max = float(input("Ruxsat etilgan tezlik: "))
oshish = v - v_max
if oshish <= 0:
    jarima = 0
elif oshish <= 20:
    jarima = 100
elif oshish <= 40:
    jarima = 200
else:
    jarima = 500
print("Jarima: $", jarima)
