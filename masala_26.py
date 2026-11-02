# Savol: (X, Y) nuqta qaysi chorakda joylashganini toping.
# Yechim: X va Y ning musbat yoki manfiyligiga qarang.
x = float(input("X = "))
y = float(input("Y = "))
if x > 0 and y > 0:
    print("I chorak")
elif x < 0 and y > 0:
    print("II chorak")
elif x < 0 and y < 0:
    print("III chorak")
elif x > 0 and y < 0:
    print("IV chorak")
elif x == 0 and y == 0:
    print("Koordinata boshi")
else:
    print("Nuqta koordinata o'qida")
