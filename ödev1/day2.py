from human import Human


faiz = 1.59
vade = "36"
krediAdi = "ihtiyac kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))


print(int(vade) + 12)
#print(int(krediAdi))
faiz = str(faiz)
print(type(faiz))

vade = int(input("Lutfen istediginiz vade sayisini giriniz: "))
print(type(vade))
vade = vade + 12

#string interpolation
#sectiginiz vade sonucu ortaya cikan vade:
print("sectiginiz vade sonucu ortaya cikan vade: " + str(vade))
print("sectiginiz vade sonucu ortaya cikan vade: {vadeSayisi}".format(vadeSayisi = vade))
print(f"sectiginiz vade sonucu ortaya cikan vade: {vade}")

isim = input("isim giriniz")
isim = "oguz"
metin = "merhaba {name}".format(name = isim)
print(metin)
#
#
## f-string
#metin = f"Hosgeldiniz {isim}"
#print(metin)

#listeler
#donguler
#fonksiyonlar

dizi = ["ihtiyac kredisi", 10, 5.2, True]
print(dizi)

krediler = ["ihtiyac kredisi", "tasit kredisi", "konut kredisi"]
print(type(krediler))

print(krediler[0])

print(len(krediler)) #lenght
#print(krediler[3]) hata verir

krediler.append("ozel kredi")
print(krediler)

krediler.append("x kredisi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.append("tasit kredisi")
print(krediler)


krediler.remove("tasit kredisi")
print(krediler)

krediler.extend(["y kredisi", "z kredisi"])
print(krediler)

#for
#i = 0 i < 10 

for i in range(10):
    print("xx")
    print(i)
print("************")

for i in range(5, 10):
    print(i)
print("*************")

for i in range(0, 51, 10):
    print(i)
print("***********")
# for i in range(0.1, 0.5):
#    print(i)
krediler = ["ihtiyac kredisi", "tasit kredisi", "konut kredisi"]
for kredi in krediler:
    print(kredi)
print("************")
for i in range(len(krediler)):
    print(krediler[i])


#sonsuz dongu
i = 0
while i < 10:
    print("x")
    i += 1
print("y")

print("***********")

while True:
    print("X")
    break
print("***********")
i = 0

print ("****** son dongu ********")
while i < len(krediler):
    i += 1
    print(krediler[i])
    if krediler[i] == "konut kredisi":
        break

#fonksiyonlar
fiyat = 100
indirim = 20

#definition, define
def calculate():
    print(100 - 20)

def calculateWithParams(fiyat, indirim):
    print(fiyat - indirim)

def sayHello(name):
    print(f"merhaba: {name}")


calculate()
calculateWithParams(123, 45)
calculateWithParams(50, 10)
sayHello("oguz")
sayHello("arif")
sayHello("halit")


def calculateAndReturn(price, discount):
    return price - discount
yeniFiyat = calculateAndReturn(fiyat, indirim)
print(yeniFiyat)

def calculatePrice(price, discount):
    print(price - discount)

def calculatePriceAndReturn(price, discount):
    return price - discount
print("********")
#fonk1 = calculatePrice(100, 20)
fonk2 = calculatePriceAndReturn(300, 100)
#print(f"fonk1: {fonk1+100}")
print(f"fonk2: {fonk2+100}")
print("**************")


#siniflar => classlar
#modules
#paket yonetimi
#self => this


#instance => ornek
human1 = Human("Enes")
human1.talk("merhaba")
human1.walk()
print(human1)

human2 = Human("Cem")
human2.talk("Selam")
human2.walk()
print(human2)

Human("Melike").talk("Merhaba")
