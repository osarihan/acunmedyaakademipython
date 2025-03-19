def tnumsum():
    a = int(input("ilk sayiyi girin: "))
    b = int(input("ikinci sayiyi girin: "))
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / 2)

#tnumsum()

def palindrom():
    word = input("kelimeyi girin: ")
    reversed_word = word[::-1]
    if (reversed_word == word):
        print("palindrom")

#palindrom()

def ageCalc():
    age = int(input("Yasinizi girin: "))
    if (age >= 100):
        return
    a = 100 - age
    print(f"{a} sene sonra 100 yasinda olacaksiniz.")
    
ageCalc()