atnese = int(input("Po kiek obuolių atsinešė mokiniai? "))
mokytojos = 20
atiteks_po = atnese + mokytojos // 8
visi = atnese * 7 + mokytojos
liko = visi % atiteks_po
print(f"liks obuolių: {liko}")
