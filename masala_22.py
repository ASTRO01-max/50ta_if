# Savol: Yil kabisa yili yoki oddiy yil ekanini aniqlang.
# Yechim: 400 ga bo'linadigan yoki 4 ga bo'linib 100 ga bo'linmaydigan yil kabisa.
yil = int(input("Yil: "))
if yil % 400 == 0 or (yil % 4 == 0 and yil % 100 != 0):
    print("Kabisa yili")
else:
    print("Oddiy yil")
