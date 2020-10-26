def kareleritoplamı(sayi):
    toplam=0
    for i in range(sayi+1):
        toplam+=i*i
    return toplam
def toplamlarınkaresi(sayi):
    toplam=0
    for i in range(sayi+1):
        toplam+=i
    return toplam*toplam

print(toplamlarınkaresi(100)-kareleritoplamı(100))