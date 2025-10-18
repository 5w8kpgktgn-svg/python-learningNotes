# numbers=[1,2,3,4,5]
# for num in numbers:   #ALT ALTA YAZILMSINI SAĞLAR
#     print(num)

# names=["cınar","sakıd","sena"]
# for na in names:
#     print(f"man name is {na}")   #f string demek virgül koymaya gerek yok demek

# isim="emirham"
# for n in isim:
#     print(n)                       #her bir harfi tek tek yazıyor

# ÖRNEKLER
sayılar=[1,3,5,7,9,12,19,21]
#1-hangi sayılar 3 ün katıdır
# for sayı in sayılar:                        
#     if (sayı % 3 == 0):      #sayılar listesinin tüm karakterleri için döndürülmüş hali
#         print(sayı)          #sayı dır ve biz sayıyı 3 ile tam bölünebiliyorsa yazdıracağız

#2-listedeki sayıların toplamı kaçtır
# toplam=0
# for sayı in sayılar:
#     toplam += sayı   #sayıların döngüsünü belirten sayı listesinin her bir değeri toplayıp         
#     print(toplam)    #toplamın içine atacak döngü ile aynı satırda olursa her eklemeyi gösterir

#     toplam=0
# for sayı in sayılar: #ama eğer alttaki gibi print değri döngü formulünün dışıında olursa
#     toplam += sayı   #sadece en son hepsinin toplanmış halini gösterir        
# print(toplam)


#3-listedeki tek sayıların karesini alınız
# for sayı in sayılar:
#      if (sayı % 2 == 1):
#          print(sayı ** 2)

# 4-sehirler=["kocaeli","istanbul","ankara","izmir","rize"]
#şehirlerden hangileri en fazla beş karakterlidir
# for sehir in sehirler:
#     if (len(sehir) <= 5):     #len() bize karakter sayısını gösterir
#         print(sehir)

# urunler=[   
# {"name":"sansung s6","price":"3000"},
# {"name":"sansung s7","price":"4000"},
# {"name":"sansung s8","price":"5000"},
# {"name":"sansung s9","price":"6000"},
# {"name":"sansung s10","price":"7000"}
# ]
#5-ÜRÜNLERİN FİYATLARI TOPLAMI NEDİR
# toplam=0
# for urun in urunler:
#     fiyat=int(urun["price"])
#     toplam+=fiyat
# print(toplam)

#6-ÜRÜNLERDEN FİYATI EN FAZLA 5000 OLAN ÜRÜNLERİ GÖSTERİNİZ
# for urun in urunler:
#     fiyat=int(urun["price"])
#     if (fiyat <= 5000):
#         print(urun["name"])

#  WHİLE DÖNGÜSÜ ------------------------------------
#  (bitiş şartı koy ya da sonsuza dek devam et)

# x=0
# while x <= 99:
#     x += 1
#     print(x)


# x=0
# while x <= 99:
#     if x % 2 == 0:
#       print(x)        #burada x+=1 ifadesini kullanmamızın nedeni x ifadesi 99 a doğru yaklaşsın diye yoksa x ekrana hep 0 olarak yazılır.kodun anlamı x i bir bir arttırırken çift ola değerlei
#     x+=1               ekrana yazdır dedik o yüzden arttırıken sadece çift olanları yazdırır ama else ile tekleride yazdırabiliriz


# x=0
# while x <= 99:
#      if x % 2 == 1:
#        print(f"tek sayı {x}")
#      else:
#         print(f"çift sayı {x}")        
#      x+=1

# name="" #false dir yani bilgisayar bunu yanlış olarak anlar
# while not name: #yani bu not name demek yanlış olmayana kadar yani name nin içi boş yani namenin tersi olana kadar yani içi dolana dakar
#     name=input("isminizi girin")
# print(f"merhaba,{name}")

# name="" 
# while not name.strip():               #eğer burada kişi boşluk karakterine basrsa çıktı (merhana,  ) olarak çıkar yani boşluğu bir isim olarak algılar bunu engellemek için ise name.strip() 
#      name=input("isminizi girin")     #karakteri kullanırız ki boşluğu bir değer olarak algılamasın
# print(f"merhaba,{name}")

#örnekler
# sayılar=[1,3,5,7,9,12,19,21]
#1-sayılar listesini while ile ekrana yazdır
# i=0  #bu bir indeksdir ve biz i ye 0 endeksini veriyoruz
# while(i < len(sayılar)):    #özet olarak i 0. endeks,biz indeksleri birer birer arttır dedik, ve bitme şartını sayılar listesinin indeksini geçme olarak koyduk,indeksleri birer birer 
#     print(sayılar[i])       #arttıracak ve denk geldiği sayıları ekrana yazacak
#     i += 1  #burada 0 indeksinden başlayarak indeksleri birer birer arttır


#2-başlangıç ve bitiş değerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın
# x=int(input("başlangıç:"))
# y=int(input("bitiş:"))
# i=x
# while(i < y):
#   if (i % 2 == 1 ):   #özet olara indeksi başlangıç yani x ile başlatttım sonra indeksleri birer birer arttır dedim,bitiş şartı olarak ise indeks bitiş indeksine yani y ye eşit olana kadar
#     print(i)          #devam et dedim ve eğer indeksler tek ise ekrana yazdır dedim

#   i+=1

#3- 1 ile 100 arasındaki sayıları azalan şekilde yazdırın.
# i=100
# while(i > 0):   #indeks değerini 100 verdim,ve birer birer azaltmasını söyledim,bitiş şartı olarak ise indeks sıfırn altına inmesin dedim ve yazdırdım
#     print(i)
#     i-=1
    
#4-kullanıcıdan alacağınız 5 sayıyı ekrana sıralı bir şekilde yazdırın
# a=int(input("sayı1:"))
# b=int(input("sayı2:"))
# c=int(input("sayı3:"))    #bu normalde yapacağımız bir işlem
# d=int(input("sayı4:"))
# e=int(input("sayı5:"))
# adam=[a, b, c, d, e]
# adam.sort()
# print(adam)

# liste=[]
# i=0
# while (i < 5 ):
#     i+=1
#     sayı=int(input("sayı:"))    #while ile hazırlanmış hali daha profesyonel duruyor
#     liste.append(sayı)
#     liste.sort()
# print(liste)


#5-kullanıcıdan alacağınz sınırsız ürün bilgisini urunle listesi içine saklayı
# (ürün sayısı kullanıcıya sorun,dictionary liste name price şeklinde olsun,ürün ekleme işlemi bittiğinde ürünleri ekrana while ile listeleyin)
# urunler=[]
# adet=int(input("kaç adet ürün istiyorsunuz:"))
# i=0
# while (i < adet):
#      x= input("name:")
#      y= int(input("price:"))
#      urunler.append([x,y])
#      i+= 1
# print(urunler)

# urunler=[]
# x=int(input("kaç adet ürün istersiniz:"))
# i=0
# while (i < x ):
#     a=input(f"{i+1}.ürünün ismi:")                 #daha profesyonel hali
#     b=input(f"fiyatı:")
#     i+= 1
#     urunler.append([a,b])
# for ur in urunler:
#  print(f"{ur[0]} - {ur[1]}")

#ekstra bir örnek güzel örnek

# 1 den 100 e kadar tek sayıların toplamı
# x=1
# toplam=0
# while (x < 100 ):
#     if (x % 2 == 1):
#      toplam+= x
    
#     x+= 1
# print(toplam)



#break ve continue ifadeleri ---------
# name = "emirhan"
# for na in name:
#     if na == "r":            # break r harfine geldi mi durdurur ama eğer break yernine continue yazsaydım r yi atlar ve diyer harfleri yazmaya devam ederdi
#         break
#     print(na)

#range() metodu
# for i in range(19):
#  print(i)

# for i in range(19,31):
#     print(i)

# for i in range(19,30,2):
#     print(i)

# print(list(range(19,30)))

#enumerate() kullanımı
# adam="hello"
# for na in enumerate(adam):
#     print(na)





#bir listede birden fazla istek

# numbers= [x * x for x in range (10) ]                    #bu ve alttakigibi bir çok koşulu böyle liste içerisine yazdırabiliriz
# print(numbers)

# numbers= [x * x for x in range (10) if (x % 3 == 0) ]
# print(numbers)


# isim="hello"
# liste=[]

# for kal in isim:
#     liste.append(kal)                      #birbirlerinin aynısı 
# print(liste)

# kısayol=[liste for liste in isim]
# print(kısayol)

# yıl=[1983,1999,2008,1956,1986]
# hesap=[2019-yaş for yaş in yıl]
# print(hesap)

# sayfa= [ x if x % 2 == 0 else "bu sayı çift değil" for x in range(1,10) ]    #köşeli parantez kullandığımıza dikkat edelim
# print(sayfa)





#örnek soru MÜKEMMEL BİR ÖRNEK
# 1 ile 100 arasında rastgele üretilecek bi sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.
#(100 üzerinden bir puanlama yapın) ve (hak bilgisini kullanııdan isteyin ve her soru belirtilen can sayısı üzerinden hesaplansın)
#(random modülü için python random şeklinde arama yapın)

# import random
# sayı= random.randint(1,100)
# hak= int(input("kaç hakta bulmak istiyorunuz:"))
# puan= 100 / hak
# i=0
# while (i < hak):
#     gir= int(input("hadi sayıyı bulun:"))
     
#     if (gir > sayı):
#         print("lürfen daha düşük bir değer deneyin",)
#     elif (gir < sayı):
#         print("lütfen daha büyük bir sayı deneyin")
#     else:
#         print("tebrikler doğru tahmin")
#         break
#     i+=1
# sonuç= (100 - (puan * i))
# print(sonuç)


# ÖRNEK SORU 2
#GİRİLEN BİR SAYININ ASAL OLUP OLMADIĞINI BULUN
# gir=int(input("lütfen bir sayı girin:"))
# if ( gir <= 1):
#     print("asal sayı değiş")
# else:
#     for i in range(2,gir):
#         if (gir % i == 0):
#             print("asal sayı değil")       #(asal sayı) ifadesinde if bağlacı olmadığı için liste döndüğü yere kadar asal sayı değil yazardı eğer else yi for un himayesinden çıkarmasaydık
#             break
#     else:    
#         print("asal sayı")












    








    




