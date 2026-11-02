# Savol: To'rt xonali son palindrom ekanini tekshiring.
# Yechim: Birinchi va oxirgi, ikkinchi va uchinchi raqamlarni solishtiring.
n = int(input("To'rt xonali son: "))
n = abs(n)
if n // 1000 == n % 10 and n // 100 % 10 == n // 10 % 10:
    print("Palindrom")
else:
    print("Palindrom emas")
