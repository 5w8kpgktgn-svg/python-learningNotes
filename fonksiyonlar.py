# def sayhello(name):
#     print("hello",name)
# sayhello("emirhan")
# sayhello("aysel")


# def sayhello(name):
#     return "hello " + name   #aşağıda ve yukarıda def in kullanım yollaı
# msg=sayhello("emirhan")
# print(msg)


# def total (num1,num2):
#     return(num1+num2)
# msg=total(19,40)
# print(msg)


# def yaşhesapla(doğumyılı):
#     return (2019 - doğumyılı)
# ada=yaşhesapla(1999)
# ali=yaşhesapla(1969)
# ata=yaşhesapla(1989)
# print(ada,ali,ata)

# def yaşhesapla(doğumyılı):
#     return (2019 - doğumyılı)

# def emekliligekacyıl(doğumyılı,isim):
#     yas=yaşhesapla(doğumyılı)
#     hesap= 65 - yas
#     if (hesap > 0):
#         print(f"{isim} kişisinin emekliliğe kalan süresi {hesap}")
#     else: 
#         (hesap < 0)
#         print(f"{isim} kişisi zaten emekli")
# emekliligekacyıl(1950,"emirhan")


# def cahnge(n):
#     n[0]="istanbul"
# sehirler=["ankara","izmir"]
# cahnge(sehirler)
# print(sehirler)


# def add(*hepsi):
#     return sum(hepsi)           # iki özekkik   
# msg=add(10,20,50,60)            # 1- sum() tüm değerlei topla        
# print(msg)                      # 2- *... ifadesi listeye ne kadar eklenirse hepsini al demek



# def kullanıcı(**sözlük):                                    #üç özellik var
#     for key,value in sözlük.items():                        # 1- **.... dictionary e çevirir
#         print("{} is {}".format(key,value))                 # 2- .items() anahtar ve değeri alır 
#                                                             # 3- .format() dictionaryden alınan anahtar ve değer leri yazdırma biçimidir

# kullanıcı(name="çınar",age="2",city="istanbul")
# kullanıcı(name="ada",age="2",city="ankara")
# kullanıcı(name="yiğit",age="2",city="izmir",phone="123")


#örnek sorular
# 1- gönderilen bir kelimeyi belirtilen kez ekrana gösteren fonkisyon yazın
# def kelime(name,adet):
#     print(name * adet)
# kelime("merhaba ",10)
    
# 2- kendine gönderilen sınırsız sayıdaki parametriyi bir listeye çeviren fonksiyon yazın
# def parametre(*çevir):
#     liste=[]
#     liste.append(çevir)                        #unutma (*çevir) amacı listeye çevir değil,sınırsız sayıdaki bilgiyi al demek
#     print(liste)
# parametre(10,40,"aysel","kullanıcı",500)



# def parametre(*çevir):
#     liste=[]                                    #3 farklı yol
#     for çev in çevir:
#         liste.append(çev)
#     return liste

# kal=parametre(10,40,"aysel","kullanıcı",500)
# print(kal)


# parametre(10,40,"aysel","kullanıcı",500)
# print(list(parametre))





# 3- gönderilen 2 sayı arasındaki tüm asla sayıları bulun
# sayı1=int(input("sayı1:"))
# sayı2=int(input("sayı2:"))
# def gönder(sayı1,sayı2):
#  for i in range(sayı1,sayı2+1):
#    if (i > 1):
#      for dol in range(2,i):
#        if (i % dol == 0):
#          break
#      else:
#        print(i)
# gönder(sayı1,sayı2)

                

            
# 4- kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürün
# sayı=int(input("sayı:"))
# def gönder(sayı):
#  if (sayı >= 1):
#     for i in range(1,sayı+1):
#       if (sayı % i == 0):
#           print(i)
# gönder(sayı)


###################################################


# LAMBDA EXPRESSİONS , MAP VE FİLTER KONUSU

# numbers=[1,3,5,9]
# islem=list(map(lambda a: a ** 2,numbers))    #map ile listenin bütün elemanlarına aynı işlemi yaparız lambda ise map ile kullanılar bir fonksiyon
# print(islem)                                 #map kullanırken list veya for kullanmak zorundayız.ikisinin kullanılmış hali 
# veya
# islem=(map(lambda a: a ** 2,numbers))
# for i in islem:
#     print(i)


# numbers=[1,3,5,9,10,15,14,17,26]
# def kural(sayı):return sayı%2==0
# ksy=list(filter(kural,numbers))
# print(ksy) 

# numbers=[1,3,5,9,10,15,14,17,26]
# ksy=list(filter(lambda kum: kum%2==0,numbers))
# print(ksy)


########################################################
# isim="ülker"
# def isimdeğiştir(kal):
#     isim=kal
#     print(kal)
# isimdeğiştir("milk")            #bir ana değeri fonksiyon içinde değiştirebiliriz ama gerçekte hala aynısı gibi kalır
# print(isim)                     #ama fonksiyonun içinden gerçek değerini de değiştirebilmemiz için (global) ifadesini kullanmalıyız


# isim="ülker"
# def isimdeğiştir(kal):
#     global isim
#     isim=kal
#     print(kal)
# isimdeğiştir("milk")
# print(isim)
    
########################################################

#BANKAMATİK ÖRNEĞİ
#kullanıcı para çekecek bakiye yetrimorsa ek hesaba geçmet ister misiniz diye soru sorulacak
#eğer geçmek ister ve yeterliyse parayı çekecek yoksa çekemeyecek
# sadıkhesap={
#     "ad":"sadık turan",
#     "hesapNO":"13245678",
#     "bakiye":3000,
#     "ekhesap":2000
# }


# eminegülberberhesap={
#     "ad":"emine gül berber",
#     "hesapno":"12345678",
#     "bakiye":2000,
#     "ekhesap":1000
# }
# def paraçek(hesap,miktar):
#     print(f"merhaba {hesap['ad']}")

#     if hesap["bakiye"] >= miktar:
#         hesap["bakiye"] -= miktar
#         print(f"hesabınızdan {miktar} tl çekilmiştir,kalan bakiye {hesap["bakiye"]} tl dir ")
#     elif hesap["bakiye"] < miktar:
#         print(f"maalesef hesabınızın bakiyesi yetersizdir")
#         toplam = hesap["bakiye"] + hesap["ekhesap"]
#         if toplam >= miktar:
#             karar=input("ek bakiyenizi kullanmak ister misiniz (evet/hayır):")
#             if karar == "evet":
#                 gerek=miktar - hesap["bakiye"]
#                 hesap["bakiye"]=0
#                 hesap["ekhesap"] -= gerek
#                 print(f"hesabızıdan {miktar} tl çekilmiştir,ek hesabınızda kalan para {hesap["ekhesap"]} tl dir")
#             elif karar == "hayır":
#                 print(f"tamam ek bakiye kullanılmıyor,bakiyeniz yetersiz")

# hesapismi=input(f"lütfen hesap isminizi girin (emine gül berber/sadık)")
# if hesapismi == "emine gül berber":
#     miktar=int(input("çekmek istediğiniz miktarı girin:"))
#     paraçek(eminegülberberhesap,miktar)
# elif hesapismi == "sadık":
#     miktar=int(input("çekmek istediğiniz miktarı girin:"))
#     paraçek(sadıkhesap,miktar)
# else:
#     print("geçersiz hesap ismi")

                
            
        

        
        
        

    
    






