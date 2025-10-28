def hazırla(tur):
    print(f"{tur} hazırlanıyor...")
def fiyat(tur):
    fiyatlar={"espresso": 60, "latte": 75, "americano": 55}
    return fiyatlar.get(tur.lower())