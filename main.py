#tipler
number = 10
print(number)
name = "aa"
print(name)
print(type(name))

name = 10
print(name)
print(type(name))
#operatorler
print(10 + 5)
print(1==1)
#mantiksal
#and or 

#atama operatorleri
#+=
#-=

#list
a_list = ["a", "b"]
a_list.append("c")
b_list = a_list
b_list.append("d")
print(b_list)
print(a_list)

print("*************")

#donguler
#for-while

#for -> genellikle belirli bir koleskiyon (list vb) veya aralik uzerinde iterasyon icin kullanilir
#iteration index
#pythonda scope'lari indentation berlirler
for i in range(5):
    print(i) #indentation, indent
    #forun isi
#forun disi

students = ["ahmet", "ali", "ata", "baris"]
#koleksiyonlar
for student in students:
    print(student)

text = "merhaba"

for letter in text: #string dongusu harfharf iterasyon yapar.
    print(letter)

print("*********")

for i in range(5,10):
    print(i)

print("*********")

for i in range(5, 20, 2):
    print(i)


#while -> infinite loop olusturma riskine sahiptir
#sart ile calisir(kosul)

#while(True):
#    print("Durum gecerli")


user_input = input("bir deger secin, cikmak icin q.")
while user_input != "q":
    print("girdiginiz deger" + user_input)
    user_input = input("bir deger secin, cikmak icin q.")

x = 10
while x <= 20:
    print(x)
    x += 1

#dongulerdeki keywordler
#break => kirma
for i in range(50):
    if i > 20:
        break
    print(i)
for i in range(50):
    if i == 25:
        continue
    print(i)

#kosullu ifadeler 
#if elif else

age = 18

if age >= 18:
    print("resitsiniz")
elif age == 18:
    print("tam 18siniz")
else:
    print("resit degilsinz")

logging_enabled = True
if (logging_enabled):
    print("Loglaniyor...")

#metodlar fonksiyonlar 

