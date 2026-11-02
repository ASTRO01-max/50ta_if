# Savol: Uchta son orasidagi o'rtancha qiymatni toping.
# Yechim: Yig'indidan eng katta va eng kichik sonni ayiring.
a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))
eng_katta = max(a, b, c)
eng_kichik = min(a, b, c)
ortancha = a + b + c - eng_katta - eng_kichik
print("O'rtancha son:", ortancha)
