def count():
    for i in range(1, 101):
        print(i)

#count()

def countEvens():
    for i in range(1, 101):
        if(i % 2 == 0):
            print(i)

#countEvens()

def factorial():
    num = int(input("Sayi giriniz: "))
    num2 = 1
    if(num == 0):
        print("1")
        return
    for i in range(0, num):
        num2 *= num
        num -= 1
    print(num2)

#factorial()

def asal_mi(number):
    if type(number) != int:
        #print("integer bir deger girin")
        return
    if number < 0:
       # print ("pozitif bir deger girin")
        return
    if number == 2:
        return True
    if number == 1 or number == 0:
       # print(f"{number} bir asal sayi degildir")
        return False
    i = 2
    while i < number:
        if (number % i == 0):
          #  print(f"{number} bir asal sayi degildir")
            return(False)
        i += 1
   # print(f"{number} bir asal sayidir")
    return True

def primecounter():
    for i in range(1, 101):
        if(asal_mi(i) == True):
            print(i)

#primecounter()