# Savol: Uchburchakni teng tomonli, teng yonli yoki turli tomonli deb aniqlang.
# Yechim: Avval uchburchak shartini, keyin tomonlar tengligini tekshiring.
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Uchburchak mavjud emas")
elif a == b and b == c:
    print("Teng tomonli")
elif a == b or a == c or b == c:
    print("Teng yonli")
else:
    print("Turli tomonli")
