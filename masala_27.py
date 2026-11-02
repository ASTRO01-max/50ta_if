# Savol: Berilgan uchta tomondan uchburchak yasash mumkinligini tekshiring.
# Yechim: Har ikki tomon yig'indisi uchinchi tomondan katta bo'lishi kerak.
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("Uchburchak yasash mumkin")
else:
    print("Uchburchak yasab bo'lmaydi")
