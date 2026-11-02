# Savol: 100 000 so'mdan oshsa 5%, 500 000 so'mdan oshsa 10% chegirma hisoblang.
# Yechim: Avval 500 000 chegarasini tekshiring, so'ng chegirmani ayiring.
summa = float(input("Xarid summasi (so'm): "))
if summa > 500000:
    chegirma = summa * 10 / 100
elif summa > 100000:
    chegirma = summa * 5 / 100
else:
    chegirma = 0
print("Chegirma:", chegirma, "so'm")
print("To'lov:", summa - chegirma, "so'm")
