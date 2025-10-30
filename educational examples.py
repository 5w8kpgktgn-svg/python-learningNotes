# ŞİFRE OLUŞTURMA

# def parola(şifre):
#     import re
#     if len(şifre) < 8:
#         raise Exception("şifre en az 8 karakterli olmalıdır")
#     elif not re.search("[a-z]",şifre):
#         raise Exception("şifrede küçük harf olmalıdır")
#     elif not re.search("[A-Z]",şifre):
#         raise Exception("şifrede büyük harf olmalıdır")
#     elif not re.search("[0-9]",şifre):
#         raise Exception("şifrede rakam olmalıdır")
#     elif re.search("\s",şifre):
#         raise Exception("şifrede boşluk olmamalıdır")
# while True:
#   cevap=input("lütfen şifre oluşturun")
#   try:
#     parola(cevap)
#   except Exception as ex:
#     print(ex)
#   else:
#       print("şifre başarılı bir şekilde oluşturuldu")
#       break

#####################################################
# QUİZ 
 
# class Soru:
#     def __init__(self,yazi,şık,cevap):
#         self.yazi=yazi
#         self.şık=şık
#         self.cevap=cevap
#     def kontrol(self,gelen):
#         return self.cevap.lower() == gelen.lower()
    
# class Quiz:
#     def __init__(self,sorular):
#         self.sorular=sorular
#         self.puan=0
#         self.index=0
#     def sorudöndür(self):
#         return self.sorular[self.index]
#     def göster(self):
#         soru=self.sorudöndür()
#         print(f"soru {self.index + 1}: {soru.yazi}")
#         for g in soru.şık:
#             print(f"- {g}")
#         alınancevap=input("cevap:")
#         self.cevapdurumunagöreyazdırma(alınancevap)
#     def cevapdurumunagöreyazdırma(self,alınancevap):
#         soru=self.sorudöndür()
#         if soru.kontrol(alınancevap):
#             self.puan += 1
#         else:
#             pass
#         self.index += 1
#         self.devamlılık_durumu()
#     def devamlılık_durumu(self):
#         if self.index == len(self.sorular):
#             print(f"puan:{self.puan}")
#         else:
#             self.göster()


# s1 = Soru("En iyi programlama dili?", ["Python", "C#", "JavaScript", "Java"], "python")
# s2 = Soru("En popüler programlama dili?", ["C#", "Python", "JavaScript", "Java"], "python")
# s3 = Soru("En çok kazandıran programlama dili?", ["C#", "Python", "Java", "JavaScript"], "python")
# liste=[s1,s2,s3]
# kal=Quiz(liste)
# kal.göster()
###########################################################
# FİLM
# “Soru” sınıfı: ipucu (yazi) ve doğru cevap (dogru) 

# class Soru:
#     def __init__(self,yazi,cevap):
#         self.yazi=yazi
#         self.cevap=cevap
#     def kontrol(self,gelen):
#         return self.cevap.lower() == gelen.lower()
    
# class Quiz:
#     def __init__(self,sorular):
#         self.sorular=sorular
#         self.puan=0
#         self.index=0
#     def döndür(self):
#         return self.sorular[self.index]
#     def göster(self):
#         soru=self.döndür()
#         print(f"soru {self.index + 1}: {soru.yazi}")
#         alınancevap=input("cevap:")
#         self.cevap_durumu(alınancevap)
#     def cevap_durumu(self,gelen):
#         soru=self.döndür()
#         if soru.kontrol(gelen):
#             self.puan += 1
#         else:
#             pass
#         self.index += 1
#         self.nereye_kadar()
#     def nereye_kadar(self):
#         if self.index == len(self.sorular):
#             print(f"puan:{self.puan}")
#         else:
#             self.göster()

# a1=Soru("size bir ip ucu verilecek ve siz filmi/diziyi tahmin edeceksiniz,ipucu:Bir adam rüyalarında bilinç altına girerek fikir çalıyor","inception")
# a2=Soru("ipucu:Kölelikten kaçan bir adam gladyatör olur","gladiator")
# a3=Soru("ipucu:Bir öğretmen kimya bilgisiyle uyuşturucu üretmeye başlar","breaking bad")
# liste=[a1,a2,a3]
# kal=Quiz(liste)
# kal.göster()
#############################################################
# BANKAMATİK

# class Hesap:
#     def __init__(self,isim,bakiye,ekbakiye):
#         self.isim=isim
#         self.bakiye=bakiye
#         self.ekbakiye=ekbakiye
#     def paraçekme(self,para):
#         if self.bakiye >= para:
#             self.bakiye -= para
#             print(f"Hesabınızdan {para}tl çekilmiştir")
#         else:
#             toplam= self.bakiye + self.ekbakiye
#             if toplam >= para:
#                 gelen=input("ekbakiyeyi kullanmak ister misiniz(evet/hayır):")
#                 if gelen == "evet":
#                     kalan= para - self.bakiye
#                     self.bakiye=0
#                     self.ekbakiye -= kalan
#                     print(f"Hesabınızdan {para}tl çekilmiştir")
#                 else:
#                     pass
#             else:
#                 print(f"üzgünüz,bakiyeniz yetersiz")
#     def bakiye_göster(self):
#         print(f"Ana baiye:{self.bakiye},Ekbakiye:{self.ekbakiye}")
# emirhan=Hesap("emirhan",2000,1000)
# ali=Hesap("ali",1000,500)
# emirhan.paraçekme(4000)
# emirhan.bakiye_göster()
##################################################################
# LAMBDA,MAP VE FİLTER 

# numbers=[1,3,5,9]
# islem=list(map(lambda a: a ** 2,numbers))    
# print(islem) 

# numbers=[1,3,5,9,10,15,14,17,26]
# ksy=list(filter(lambda kum: kum%2==0,numbers))
# print(ksy)
###################################################################
# SAYI TAHMİN OYUNU

# import random
# sayı= random.randint(1,10)
# hak=int(input("bu sayıyı kaç hakta tahmin edersiniz"))
# puan=100
# eksil= 100 / hak
# i = 0
# while i < hak:
#     tahmin=int(input("tahnin edin:"))
#     if tahmin >sayı:
#         print("lütfen daha küçük bir sayı tahmin edin")
#     elif tahmin < sayı:
#         print("lütfen daha büyük bir sayı tahmin edin")
#     else:
#         print("tebrikler doğru bildiniz")
#         break
# i += 1    
####################################################################
# DERS PUANI YAZDIRMA

# def hesap(gelen):
#     gelen=gelen.strip()
#     liste=gelen.split(":")
#     adsoyad=liste[0]
#     notlar=liste[1].split(",")
#     notlar=[int(x)for x in notlar]
#     ortalama= sum(notlar) / len(notlar)
#     if ortalama>=90 and ortalama<=100:
#         harf="AA"
#     elif ortalama>=85 and ortalama<=89:
#         harf="BA"
#     elif ortalama>=65 and ortalama<=84:
#         harf="cc"
#     else:
#         harf="FF"
#     return f"ortalama:{ortalama:.2f}({harf})"

# def ortalamaları_oku():
#     with open("dosya.txt","r",encoding="utf-8") as file:
#         for i in file:
#             print(hesap(i))
# def not_gir():
#     ad=input("ad:")
#     soyad=input("soyad:")
#     not1=input("not1:")
#     not2=input("not2:")
#     not3=input("not3:")
#     with open("dosya.txt","a",encoding="utf-8") as file:
#         file.write(ad+" "+soyad+":"+not1+","+not2+","+not3+"\n")
# def notları_kayıtet():
#     with open("dosya.txt","r",encoding="utf-8") as file:
#         liste=[]
#         for b in file:
#             liste.append(hesap(b))
#     with open("sonuclar.txt","w",encoding="utf-8") as file2:
#         for k in liste:
#             file2.write(k+"\n")
# while True:
#     islem=input("1-notları oku\n2-notları gir\n3-notları kayır et\n4-çıkış\n")
#     if islem == "1":
#         ortalamaları_oku()
#     elif islem == "2":
#         not_gir()
#     elif islem == "3":
#         notları_kayıtet()
#     else:
#         break
#########################################################################

