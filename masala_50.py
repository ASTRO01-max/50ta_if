# Savol: So'mni USD, EUR yoki RUB valyutasiga aylantiring.
# Yechim: Kurs matnda berilmagan, shuning uchun uni foydalanuvchidan so'rang.
valyuta = input("Valyuta (USD/EUR/RUB): ")
if valyuta == "USD" or valyuta == "EUR" or valyuta == "RUB":
    summa = float(input("Summa (so'm): "))
    kurs = float(input("1 valyuta birligi uchun so'm kursi: "))
    if kurs > 0:
        print("Natija:", summa / kurs, valyuta)
    else:
        print("Kurs musbat bo'lishi kerak")
else:
    print("Noto'g'ri valyuta")
