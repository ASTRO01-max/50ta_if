# Savol: Oy raqamiga qarab faslni aniqlang.
# Yechim: Oylarni fasl bo'yicha guruhlang.
oy = int(input("Oy raqami (1-12): "))
if oy == 3 or oy == 4 or oy == 5:
    print("Bahor")
elif oy == 6 or oy == 7 or oy == 8:
    print("Yoz")
elif oy == 9 or oy == 10 or oy == 11:
    print("Kuz")
elif oy == 12 or oy == 1 or oy == 2:
    print("Qish")
else:
    print("Noto'g'ri oy")
