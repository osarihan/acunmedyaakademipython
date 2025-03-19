def makeList():
    elist = list()
    for i in range(1, 6):
        elist.append(int(input(f"{i}. sayiyi girin: ")))
    
    total = sum(elist)
    print(f"toplam: {total}")
    maxn = max(elist)
    print(f"en buyuk sayi: {maxn}")
    minn = min(elist)
    print(f"en kucuk sayi: {minn}")
    avg = sum(elist) / len(elist)
    print(f"ortalamalari: {avg}")
    
#makeList()

def makeList2():
    elist = list()
    while True:
        word = input("bir kelime gir ya da cikmak icin 'q' yaz: ")
        if(word == 'q'):
            break
        elist.append(word)
    elist.reverse()
    print(elist)

#makeList2()

def listChecker(asd):
    x = len(asd)
    i = 0;
    while(i < len(asd)):
        b = asd[i]
        a = i + 1
        while(a < len(asd)):
            if(b == asd[a]):
                asd.pop(a)
            else:
                a += 1
        i += 1
    print(asd)

numbers = [1, 2, 3, 2, 4, 5, 3, 1, 6, 2]

fruits = ["elma", "armut", "kiraz", "elma", "muz", "armut", "çilek"]
listChecker(fruits)
listChecker(numbers)