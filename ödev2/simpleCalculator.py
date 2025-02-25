def hesap_makinesi(num1, num2, sem):
    if sem != '+' and sem != '/' and sem != '*' and sem != '-':
        print("Geçersiz işlem türü!")
        return
    if type(num1) != int or type(num2) != int:
        print("1. ve 2. parametreler sayi olmalidir")
    if sem == '/' and num2 == 0:
        print("Bölme işlemi için ikinci sayi 0 olamaz!")
        return
    if sem == '+':
        print(num1 + num2)
        return(num1 + num2)
    if sem == '-':
        print(num1 - num2)
        return(num1 - num2)
    if (sem == '*'):
        print(num1 * num2)
        return(num1 * num2)
    if (sem == '/'):
        print(num1 / num2)
        return(num1 / num2)

hesap_makinesi(5, 3, '+') # Çıktı: 5 + 3 = 8
hesap_makinesi(10, 2, '/')  # Çıktı: 10 / 2 = 5.0
hesap_makinesi(4, 0, '/')  # Çıktı: Bölme işlemi için ikinci sayı 0 olamaz!
hesap_makinesi(6, 2, '%')  # Çıktı: Geçersiz işlem türü!
hesap_makinesi(6, 2, 'A')
hesap_makinesi(6, 2, 21)
hesap_makinesi(5, 3, '-')
hesap_makinesi(5, 3, '*')
