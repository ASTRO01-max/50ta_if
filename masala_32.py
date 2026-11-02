# Savol: A va B sonlari bir xil ishorali yoki har xil ishorali ekanini toping.
# Yechim: Ikkalasi ham musbat yoki ikkalasi ham manfiy bo'lsa ishorasi bir xil.
a = float(input("A = "))
b = float(input("B = "))
if (a > 0 and b > 0) or (a < 0 and b < 0):
    print("Ishoralari bir xil")
else:
    print("Ishoralari har xil yoki sonlardan biri nol")
