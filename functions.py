#fonksiyonlar
price = 500
total_price = price + (price * 0.2)

print(total_price)

#fonk tanimlamak

def calculate_tax(price, rate=20):
    f_variable = "deneme" #fonksiyon scopeiuna ozel
    print(f_variable)
    #print(price + (price * 0.2))
    return price + (price * (rate / 100))

price1 = calculate_tax(100)
price2 = calculate_tax(400, 30)
print(price1)

def sum(*args):
    if len(args) <= 0:
        print("en az bir sayi gondermek zorundasiniz")
        return
    sonuc = 0
    for sayi in args:
        sonuc += sayi
    return sayi

print(sum(1, 2))
print(sum (10, 20, 50, 203))
print(sum())

#*kwarg => ARASTIRILSIN

# lamda fonk
#anonim

topla = lambda a, b: a + b 

print(topla(10, 20))

selamla = lambda isim: print(f"merhaba {isim}")
print(selamla("ouz"))

#oop sonraki ders
#colab
#jupyter notebook
