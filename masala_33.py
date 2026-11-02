# Savol: [1, 100] oralig'idagi son bir, ikki yoki uch xonali ekanini toping.
# Yechim: Sonni 9, 99 va 100 chegaralari bilan taqqoslang.
n = int(input("1 dan 100 gacha son: "))
if n >= 1 and n <= 9:
    print("Bir xonali")
elif n >= 10 and n <= 99:
    print("Ikki xonali")
elif n == 100:
    print("Uch xonali")
else:
    print("Noto'g'ri son")
