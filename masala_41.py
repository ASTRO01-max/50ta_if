# Savol: Berilgan sanadan keyingi kunni toping.
# Yechim: Kun sonini bittaga oshiring; oy yoki yil tugasa sanani yangilang.
kun = int(input("Kun: "))
oy = int(input("Oy: "))
yil = int(input("Yil: "))
if oy == 1 or oy == 3 or oy == 5 or oy == 7 or oy == 8 or oy == 10 or oy == 12:
    kun_soni = 31
elif oy == 4 or oy == 6 or oy == 9 or oy == 11:
    kun_soni = 30
elif oy == 2:
    if yil % 400 == 0 or (yil % 4 == 0 and yil % 100 != 0):
        kun_soni = 29
    else:
        kun_soni = 28
else:
    kun_soni = 0
if kun < 1 or kun > kun_soni:
    print("Sana noto'g'ri")
else:
    kun = kun + 1
    if kun > kun_soni:
        kun = 1
        oy = oy + 1
        if oy > 12:
            oy = 1
            yil = yil + 1
    print(kun, oy, yil)
