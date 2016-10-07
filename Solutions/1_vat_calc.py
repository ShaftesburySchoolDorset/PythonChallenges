vat = int(input("vat?"))
total = int(input("total?"))

vat_float = float(vat) / 100.0
final_total = total * (1 + vat_float)
print(final_total)
