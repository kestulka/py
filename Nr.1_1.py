paros = int(input("Įveskite parų kiekį: "))
menesiai = paros//30
savaites = paros//7
dienos = paros%7 
print(f"Jūsų įvestas parų skaičius atitinka {menesiai} menesius | {savaites} savaites | {dienos} dienas")

