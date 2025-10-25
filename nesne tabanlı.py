# CLASS,İNİNT,SELF  HEM DEPO HEMDE SİSTEM
# aynı bankamatik örneğini birde bu ifadelerle yazalım

# class Hesap:
#     def __init__(self,ad,bakıye,ekhesap):
#         self.ad=ad
#         self.bakıye=bakıye
#         self.ekhesap=ekhesap

#     def paraçekme(self,miktar):                                           #class,init,self bunlar bilgiyi depolma ve kullanmamıza yarar.init bilgileri kayıt etme aşamasıdır
#         print(f"merhaba {self.ad}")                                       #paraçekme(self) diye brakırsak fonksiyonu ditek paraçekme() diye çağırabiliriz  
#         if self.bakıye >= miktar:                                         #ama eğer paraçekme(self,miktar) girersek bu sefer foksiyornu paraçekme(1000) olarak çağırmamız gerekir
#             self.bakıye -= miktar
#             print(f"{miktar} tl çekildi, kalan bakiye: {self.bakıye}")
#         else:
#             toplam=self.bakıye + self.ekhesap
#             if toplam >= miktar:
#                 print(f"işleminize ekhesap ile devam edeceğiz")
#                 kalan= miktar- self.bakıye
#                 self.bakıye=0
#                 self.ekhesap -= kalan
#                 print(f"hesabınızdan {miktar} tl çekilmiştir, ek hesabınızda kalan para: {self.ekhesap} tl dir")
#             else:
#                 print(f"üzgünüm bakiyeniz yetersiz")
    
#     def bakiyegoster(self):
#         print(f"merhaba {self.ad}")
#         print(f"Ana hesabınızda olan para: {self.bakıye}, ekhesabınızda olan para:{self.ekhesap}")


# emirhan=Hesap("emirhan",3000,1000)
# ali=Hesap("ali",1500,500)

# emirhan.bakiyegoster()
# emirhan.paraçekme(3500)
# emirhan.bakiyegoster()

# ali.paraçekme(1800)
# ali.bakiyegoster()

##############################################################################################################

# MİRAS ALMA (İNHERİTANCE):

# class soru:
#     def __init__(self,ad,soyad):
#         self.ad=ad
#         self.soyad=soyad
        

# class balta(soru):
#      def __init__(self,numara):
#          super().__init__("emirhan","berber")
#          self.numara=numara


# kayıt=balta("123")
# print(kayıt.ad)
# print(kayıt.soyad)
# print(kayıt.numara)

###############################################################################################

# bize soru bilgisini barındıran bir Question class ı yapacağız 
# ve bir Quiz classı oluşturacağız ve bu dışarıdan soruları alacak sırayla gösterecek ve
# bir skor tutacak  sonunda bu kişinin kaç skor yaptığını bize gösterecek

# Question

# class Question:
#     def __init__(self,text,choices,answer):
#         self.text=text
#         self.choices=choices                     #burada dedikki mesela dışarıdan gelen text yazısını fonksiyonun kendi sorusu olarak al yani self.text olarak
#         self.answer=answer

#     def checkanswer(self,answer):
#         return self.answer == answer             #burada dedikki bizim tanıttığımız yani fonksiyonun kendi cevabı olan self.answer dışarıdan gelen answer değerine eşitse doğru olarak adalndır dedik
    
# q1=Question("en iyi programlama dili?",["python","c#","javascript","java"],"python")
# q2=Question("en popüler programlama dili?",["c#","python","javascript","java"],"python")
# q3=Question("en çok kazandıran programlama dili?",["c#","python","java","javascript"],"python")

# print(q1.checkanswer("python"))
# print(q2.checkanswer("javascript"))
# print(q3.checkanswer("c#")                     

##############################################################
#  enumerate özel kullanım

# liste = ["Ekmek", "Süt", "Peynir", "Yumurta"]

# for i,ürün in enumerate(liste,start=1):
#     print(f"{i} ) {ürün}")

############################################################################################################################################
# FİLM
# “Soru” sınıfı: ipucu (yazi) ve doğru cevap (dogru) 

# “Quiz” sınıfı: soruları döngüyle göster, her biri için kullanıcıdan cevap iste, kontrol et, puanı arttır.

# class Soru:
#     def __init__(self,yazi,dogru):
#         self.yazi=yazi
#         self.dogru=dogru
#     def kontrol(self,gelencevap):
#         return self.dogru.lower() == gelencevap.lower()
    
# class Quiz:
#     def __init__(self,sorular):
#         self.sorular=sorular
#         self.puan=0
#         self.index=0
#     def döndür_geti_sırayla(self):
#         return self.sorular[self.index]
#     def göster(self):
#         gelen=self.döndür_geti_sırayla()
#         print(f"soru {self.index + 1}: {gelen.yazi}")
#         cevap=input("Lütfen verilen ipucuna göre bir cevap yazın:")
#         self.dogruluk_durumuna_göre_yazdırma(cevap)
#     def dogruluk_durumuna_göre_yazdırma(self,ver):
#          gelen=self.döndür_geti_sırayla()
#          if gelen.kontrol(ver):
#              self.puan += 1
#          else:
#              pass
#          self.index += 1
#          self.bitme_durumu()
#     def bitme_durumu(self):
#         if self.index == len(self.sorular):
#             print(f"Puanınız:{self.puan}")
#         else:
#             self.göster()

# a1=Soru("size bir ip ucu verilecek ve siz filmi/diziyi tahmin edeceksiniz,ipucu:Bir adam rüyalarında bilinç altına girerek fikir çalıyor","inception")
# a2=Soru("ipucu:Kölelikten kaçan bir adam gladyatör olur","gladiator")
# a3=Soru("ipucu:Bir öğretmen kimya bilgisiyle uyuşturucu üretmeye başlar","breaking bad")
# liste=[a1,a2,a3]
# kal=Quiz(liste)
# kal.göster()

#############################################################################################################################################################
# QUİZ
# class Soru:
#     def __init__(self,yazi,şıklar,cevap):
#         self.yazi=yazi
#         self.şıklar=şıklar
#         self.cevap=cevap
#     def kontrol(self,gelencevap):
#         return self.cevap.lower() == gelencevap.lower()
    
# class Quiz:
#     def __init__(self,sorular):
#         self.sorular=sorular
#         self.puan=0
#         self.index=0
#     def döndür(self):
#         return self.sorular[self.index]
#     def göster(self):
#         gelen=self.döndür()
#         print(f"soru {self.index + 1}: {gelen.yazi}")
#         for g in gelen.şıklar:
#             print(f"- {g}")
#         cevap=input("Lütfen bir cevap girin:")
#         self.dogruluk_durumunagöre_yazdırma(cevap)
#     def dogruluk_durumunagöre_yazdırma(self,cevap):
#          gelen=self.döndür()
#          if gelen.kontrol(cevap):
#              self.puan += 1
#          else:
#              pass
#          self.index += 1
#          self.nereyekadar()
#     def nereyekadar(self):
#         if self.index == len(self.sorular):
#             print(f"Puanınız: {self.puan}")
#         else:
#             self.göster()

# s1 = Soru("En iyi programlama dili?", ["Python", "C#", "JavaScript", "Java"], "python")
# s2 = Soru("En popüler programlama dili?", ["C#", "Python", "JavaScript", "Java"], "python")
# s3 = Soru("En çok kazandıran programlama dili?", ["C#", "Python", "Java", "JavaScript"], "python")
# liste=[s1,s2,s3]
# kal=Quiz(liste)
# kal.göster()