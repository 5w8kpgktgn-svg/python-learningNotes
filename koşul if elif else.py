# isim= "emirha"
# parolar= "123"
# if (isim == "emirhan") and (parolar == "123"):
#      print("hoşgeldiniz")
# else:
#      print("parola veya şifre yanlış")




# x=input("isminizi girin:")
# y=input("parolanızı giirnÇ")
# if (x == "emirhan") and (y == "123"):
#  print("hoşgeldiniz")
# else:
#     print("parola veya şifre hatalı")



#KİŞİ PAROLA MI İSİM Mİ YANLIŞ BİLMEK İSTER BUNUN İÇİN GEREKLİ KOD
# X= input("isim:")
# y= input("şifre:")
# if (X == "emirhan"):   #önce if lere bakar hangi if yanlış ise onun else ine gider eğer iki ifde yanlış ise önce dıştaki else yi gösterir eğer hepsi doğruysa iki iften sonra gelen printi yazdırır
#    if(y == "123"):                 
#        print("hoşgeldiniz")
#    else:
#        print("parola hatalı")
# else:
#     print("hatalı isim")



#FAZLALI KOŞUL VARSA
# x= int(input("x:"))
# y= int(input("y:"))
# if (x >= y):
#     print("x büyük veya eşittir y ye")
# elif (x < y):
#     print("x y den küçüktür")


# number= int(input("sayı gir:"))
# if ( number > 0 ):
#     print("pozitif")
# elif(number < 0 ):
#     print("negatif")
# else:
#     print("sayı sıfırdır")


#ÖRNEK ALIŞTIRMA
# 1-KULLANICIDAN İSİM YAŞ VE EĞİTİM BİLGİLERİNİ İSTEYİP EHLİYER ALABİLME DURUMUN KONTROL
# EDİNİZ.EHLİYER ALMA KOŞULU EN AZ 18 VE EĞİTİM DURUMU LİSE YA DA ÜNİVERSİTE OLMALIDIR.

# x=input("isim:")
# y=int(input("yaş:"))
# z=input("eğitim (LİSE YA DA ÜNİVERSİTE OLARAK YAZIN):")
# if (y >= 18) and ((z == "lise") or (z == "üniversite")):
#     print("bu kişi ehliyet alabilir")
# else:
#     print("bu kişi ehliyet alamaz")

    # YA DA
# x=input("isim:")
# y=int(input("yaş:"))
# z=input("eğitim (LİSE YA DA ÜNİVERSİTE OLARAK YAZIN):")
# if (y >= 18):
#     if ((z == "lise") or (z == "üniversite")):
#      print("bu kişi ehliyer alablir")
#     else:
#      print("bu kişi ehliyet alamaz çünkü eğitim durumu yetersiz")
# else:
#    print("bu kişi ehliyet alamaz çünkü yaşı yetersiz")


#  2- BİR ÖPRENCİNİN 2 AZILI BİR SÖZLÜ ORTALAMASIİLE GELEN NOT BİLGİSİ YAZDIRIN

# x=float(input("yazılı1:"))
# y=float(input("yazılı2:"))
# z=float(input("sözlü:"))
# ortalama= (x + y + z) / 3
# if (0 < ortalama < 24):
#     print("0")
# elif (25 < ortalama < 44 ):
#     print("1")
# elif (45 < ortalama < 54 ):
#     print("2")
# elif (55 < ortalama < 69 ):
#     print( "3")
# elif(70 < ortalama < 84 ):
#     print("4")
# elif(85< ortalama < 100):
#     print("5")

