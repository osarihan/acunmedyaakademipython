def takeInput():
    name = input("isminizi girin. ")
    age = int(input("yasinizi girin. "))
    bd = int(input("dogum yilinizi girin"))
    print(f"Merhaba {name}! {age} yasindasin ve {bd} yilinda dogmussun.")


#takeInput()

def takeTwoNum():
    num = int(input("ilk sayiyi girin."))
    num2 = int(input("ikinci sayiyi girin."))
    print(num + num2)
    print(num - num2)
    print(num * num2)
    print(num / num2)

takeTwoNum()