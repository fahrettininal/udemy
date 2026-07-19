sayi1 = 40
sayi2 = 50
sayi3 = 70

if sayi1 > sayi2 > sayi3:
    print(sayi1, sayi3)

elif sayi1 > sayi3 > sayi2:
    print(sayi1, sayi2)

elif sayi2 > sayi1 > sayi3:
    print(sayi2, sayi3)

elif sayi2 > sayi3 > sayi1:
    print(sayi2, sayi3)

elif sayi3 > sayi2 > sayi1:
    print(sayi3, sayi1)
    
else:
    print(sayi3, sayi2)

