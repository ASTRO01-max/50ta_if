# Savol: Ish stajiga qarab maoshga mukofot foizini hisoblang.
# Yechim: 2 yilgacha 0%, 2-5 yil 5%, 5-10 yil 10%, 10 yildan boshlab 15%.
staj = float(input("Ish staji (yil): "))
maosh = float(input("Maosh (so'm): "))
if staj < 2:
    foiz = 0
elif staj < 5:
    foiz = 5
elif staj < 10:
    foiz = 10
else:
    foiz = 15
mukofot = maosh * foiz / 100
print("Mukofot:", mukofot, "so'm")
print("Jami maosh:", maosh + mukofot, "so'm")
