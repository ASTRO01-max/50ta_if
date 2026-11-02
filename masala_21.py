# Savol: Ballga qarab bahoni aniqlang: 90-100: 5, 70-89: 4, 50-69: 3, 0-49: 2.
# Yechim: Ball 0-100 oralig'ida ekanini, so'ng baho chegaralarini tekshiring.
ball = int(input("Ball (0-100): "))
if ball < 0 or ball > 100:
    print("Noto'g'ri ball")
elif ball >= 90:
    print(5)
elif ball >= 70:
    print(4)
elif ball >= 50:
    print(3)
else:
    print(2)
