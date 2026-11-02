# Savol: Berilgan kun, oy, yil haqiqiy sana ekanini tekshiring.
# Yechim: Oyga mos kunlar sonini toping; fevralda kabisa yilini hisobga oling.
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
if kun >= 1 and kun <= kun_soni:
    print("Sana to'g'ri")
else:
    print("Sana noto'g'ri")
