def asal_mi(number):
    if type(number) != int:
        print("integer bir deger girin")
        return
    if number < 0:
        print ("pozitif bir deger girin")
        return
    if number == 2:
        return True
    if number == 1 or number == 0:
        print(f"{number} bir asal sayi degildir")
        return False
    i = 2
    while i < number:
        if (number % i == 0):
            print(f"{number} bir asal sayi degildir")
            return(False)
        i += 1
    print(f"{number} bir asal sayidir")
    return True

asal_mi(7)  # Çıktı: 7 bir asal sayıdır.
print("*")
asal_mi(10) # Çıktı: 10 bir asal sayı değildir.
print("*")
asal_mi("19")
print("*")
print(asal_mi(0))
print("*")
print(asal_mi(2))
print("*")
print(asal_mi(3))   
print(asal_mi(4))   
print(asal_mi(5))   
print(asal_mi(11))  
print(asal_mi(15))  
print(asal_mi(1))   
print(asal_mi(0))   
print(asal_mi(-7))
print(asal_mi(97))  
