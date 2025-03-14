def isEven():
    num = int(input("sayi giriniz "))
    if(num < 0):
        print("pozitif sayi ya da sifir girin")
        return

    if (num % 2 == 1):
        print("sayi tek sayidir")
    else:
        print("sayi cift sayidir")

#isEven()

def gradeFunc():
    grade = int(input("notunuzu girin: "))
    if (grade > 100):
        print("hata")
        return
    if (grade >= 90 and grade <= 100):
        print("A")
    elif (grade >= 80 and grade <= 89):
        print("B")
    elif (grade >= 70 and grade <= 79):
        print("C")
    elif (grade >= 60 and grade <= 69):
        print("D")
    else:
        print("F")

#gradeFunc()

def ages():
    age = int(input("yasinizi girin: "))
    if (age >= 0 and age <= 12):
        print("cocuk")
    elif (age <= 19):
        print("Genc")
    elif (age <= 59):
        print("Yetiskin")
    else:
        print("yasli")

#ages()
    
    