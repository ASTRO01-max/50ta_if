# Savol: 0-23 soatga qarab salomlashuvni chiqaring.
# Yechim: Soatni berilgan vaqt oraliqlari bilan tekshiring.
soat = int(input("Soat (0-23): "))
if soat >= 5 and soat <= 11:
    print("Xayrli tong")
elif soat >= 12 and soat <= 17:
    print("Xayrli kun")
elif soat >= 18 and soat <= 21:
    print("Xayrli kech")
elif (soat >= 0 and soat <= 4) or (soat >= 22 and soat <= 23):
    print("Xayrli tun")
else:
    print("Noto'g'ri soat")
