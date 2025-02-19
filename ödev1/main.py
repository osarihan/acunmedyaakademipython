print("hello")
baslik = "Tasit kredisi"
print(baslik)
#string metinsel ifadedir
baslik = "ihtiyac kredisi"
print(baslik)
#int, integer tam sayidir
vade = 36
ekVade = 6
vade2 = "36"

#float, decimal, double
aylikOdeme = 200.50

#bool, boolean true ya da false deger tutar
yukselIsteMi = False

#matematiksel operatorler

# +
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)

# -
print(5-5)
print(vade - 12)
print(vade - ekVade)
print(36 - 6)

# *
print(5*5)
print(vade * 2)
print(vade * ekVade)
print(10 * 10)

# /
print(5 / 5)
print(vade / 2)
print(vade / ekVade)
print(10 / 2)


yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % => mod operatoru
print(10 % 2)
print(vade % 5)
print(vade % ekVade)
print(30 % 10)


# mantiksal operatorler
print(1 == 1)
print(1 == 2)

print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)


print(1 != 1)
print(1 != 2)

# or and

# or => veya
print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)

print(1 > 2 and 5 > 2 and 3 > 2)

print(2 > 1 or 1 > 2 and 3 > 2)

# karar yapilari
#if else

sayi1 = 15
sayi2 = 15
#sayi 1 sayi2'den buyukse ekrana 1 daha buyuk yazdir

#indent
if sayi1 <= sayi2:
    print("sayi1 sayi2'den kucuktur")
#eger if bloguna girmezse
elif sayi1 == sayi2:
    print("iki sayi esittir")
#eger if ve else if bloklarindan hicbirine girmez ise
else:
    print("sayi1 sayi2'den buyuktur")

print("*****************")

if sayi1 <= sayi2:
    print("sayi1 sayi2'den kucuktur")
if sayi1 == sayi2:
    print("iki sayi esittir")
else:
    print("sayi 1 sayi 2'den kucuktur")

print("burasi if blogunun disidir.")

