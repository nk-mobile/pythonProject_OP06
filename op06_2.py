import arithmetic as ar

a = float(input("введите a : "))
b = float(input("введите b : "))

print(f"Cумма a+b {ar.my_sum(a, b)}")
print(f"Разность a-b {ar.my_sub(a, b)}")
print(f"Умножение a*b {ar.my_mul(a, b)}")
print(f"Деление a/b {ar.my_div(a, b)}")
