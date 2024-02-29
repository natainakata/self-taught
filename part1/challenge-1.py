print("one")
print("two")
print("three")

x = 26
if x < 10:
    print("10未満")
elif x >= 10:
    print("10以上")

if x <= 10:
    print("10以下")
elif x > 10 and x <= 25:
    print("10より大きく25以下")
else:
    print("25より大きい")

a = 20
b = 3
print(a % b)
print(a // b)

age = 20

if age < 18:
    print("未成年")
elif age >= 18 and age < 20:
    print("成人してるけど酒、タバコはまだ")
else:
    print("成人")
