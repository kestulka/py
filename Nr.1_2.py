from fractions import Fraction

Rolandas = float(input("Rolando pinigų suma: "))
Vilandas = float(input("Vilando pinigų suma: "))
Amandas = float(input("Amando pinigų suma: "))
picos_kaina = Rolandas + Vilandas + Amandas
# rolando_dalis = Rolandas / picos_kaina
# Vilando_dalis = Vilandas / picos_kaina
# Amando_dalis = Amandas / picos_kaina
# Arba
Rolando_dalis, Vilando_dalis, Amando_dalis = Rolandas / picos_kaina, Vilandas / picos_kaina, Amandas / picos_kaina
Rolando_dalis = round(Rolando_dalis, 2)
Vilando_dalis = round(Vilando_dalis, 2)
Amando_dalis = round(Amando_dalis, 2)
Rolando_trupmena = Fraction(Rolando_dalis).limit_denominator(10)
Vilando_trupmena = Fraction(Vilando_dalis).limit_denominator(10)
Amando_trupmena = Fraction(Amando_dalis).limit_denominator(10)
print(f"Rolandas gaus {Rolando_trupmena} picos dalį, Vilandas gaus {Vilando_trupmena} picos dalį, Amandas gaus {Amando_trupmena} picos dalį")