#ogrenci1 = "Engin"
#ogrenci2 = "Derin"
#ogrenci3 = "Salih"

#print(ogrenci1)
#print(ogrenci2)
#print(ogrenci3)

ogrenciler = ["Engin", "Derin", "Salih"]


ogrenciler.append("Ahmet")
#ogrenciler[4] ="Veli"
print(ogrenciler[3])
ogrenciler.remove("Salih")
print(ogrenciler)

#list constructor
sehirler = list(("Ankara", "İstanbul"))
print(sehirler)
print(len(sehirler))

#diğer fonksiyonlar
print(sehirler.clear())
print("Ankara sayısı = " + str(sehirler.count()))

