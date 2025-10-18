"""
x = input("bir sayı gir:")
y = input("bir sayı daha gir:")

toplam= int(x)+ int(y)

print(toplam)
"""

"""
a=input("lütfen bir sayı girin:")
b=input("lütfen bir sayı daha girin:")

sonuc= int(a) + int(b)

print("cecap:",sonuc)
"""

"""
x=input("lütfen isminizi girer misiniz:")
y=input("lütfen soy isminizi girer misiniz")

sonuc= x + ' ' + y

print("isim - soyisim:",sonuc)
"""

"""
pi= 3.14
x= int(input("bir yarı çap değeri girin:"))

alan= pi * x ** 2
çevre= 2 * pi * x
print("alan değeri:",alan)
print("çevre değeri:",çevre)
"""

"""
a= int(input("lütfen bir sayı girer misiniz:"))
b= int(input(("lütfen ilk girdiğinile çarmak istediğiniz bir sayı daha girer misiniz")))

islem = a * b

print("çarpma işleminizin sonucu:", islem) 
""

"""
#name="aysel"
#surname="berber"
#age="43"

#print(f"ismim {name} , soyismim {surname} \nve son olarak yaşım {age}")

# website= "http://www.sadiktran.com"
# course= "pyton kursu: baştan sona python programlama rehberiniz (40 saat)"
#print(len(course))
#print(website[21:24])

#name,surname,age,job= "bora","yılmaz","32","mühendis"
#print(f" benim adım {name} {surname},yaşım {age} ve mesleğim {job}")

#  x= "abc" * 3
#  print(x)

# araba = ("bmw","mercedes","supra","mazda")
# print(araba[-2])

# araba = ["bmw","mercedes","supra","mazda"]
# araba[-1]= "toyota"
# print(araba)

# araba = ["bmw","mercedes","supra","mazda"]
# print(araba[:3])

# araba = ["bmw","mercedes","supra","mazda"]
# tekerlek = araba + ["audi","ferrari"]
# print(tekerlek)

# araba = ["bmw","mercedes","supra","mazda"]
# del(araba[-1])
# print(araba)

# araba = ["bmw","mercedes","supra","mazda"]
# print(araba[::-1])

# names= ["ali","yağmur","hakan","deniz"]
# names.append("cenk")
# print(names)

# names= ["ali","yağmur","hakan","deniz"]
# names.remove("deniz")
# print(names)

# names= ["ali","yağmur","hakan","deniz"]
#us=names.index("deniz")
#print(us)
# x="ali" in names
# print(x)

#names= ["ali","yağmur","hakan","deniz"]
# names.reverse()
# print(names)
#names.sort()
#print(names)

# years=[1990,2000,1998,1987]
# x=years.count(1998)
# print(x)

# list= ["ali","ahmet"]
# list[-2]= "kuş"
# print(list)

# plakalar= {"ankara":6, "edirne":13,"adıyaman":14}
#print(plakalar["ankara"])
# plakalar["pamukkale"]= 8
# print(plakalar)
# plakalar["edirne"]= "rize: 53"
# print(plakalar)



# ogrenciler= {
#     "120":{ "ad":"", 
#            "soyad":"", 
#            " telefon":""},

#     "125":{ "ad":"can",
#            "soyad":"korkmaz",
#            "telefon":"532 000 00 02"}
# }
# ogrenciler["120"]["ad"]=input("lütfen isminizi girin:")
# ogrenciler["120"]["soyad"]=input("lütfen soyadınızı girin:")
# ogrenciler["120"]["telefon"]=input("lütfen geçerli bir telefon numarası girin:")

# bilgi= ogrenciler["120"]["ad"] , ogrenciler["120"]["soyad"] , ogrenciler["120"]["telefon"]
# ad,soyad,telefon=bilgi
# print("isim:",ad)
# print("soyisim",soyad)
# print("telefon:",telefon)

# x,y,z= 5,10,20
# x,y=y,x
# print(x,y,z)
# x=+5 ile x= x + 5 aynı şeydir

# x,y,z=2,5,10
# a=int(input("lütfen bir sayı girin:"))
# b=int(input("lütfen ilk girdiğiniz sayıyla çarmak istediğiniz bir sayı daha girin"))
# ıslem= a * b
# toplam= x + y + z
# sonuc=ıslem - toplam
# print(sonuc)

# a=y // x   bu işlem y nin x ile tam bölümünü ifade eder
# print(a)


#KARŞILAŞTIRMA OPERATÖRLERİ

# isim="sadık"
# sıfre="123"
# x= ("sdkt" == isim)
# print(x)  false
# x= ("sdkt" != isim)
# print(x)  true



#KULLANICIDAN İKİ VİZE %60 VE FİNAL %40 NOTUNU ALIP ORTALAMA HESAPLAYINIZ
# X=int(input("vize nontunuzu girin lütfen:")) 
# y=int(input("final notunuzu girin lütfen:"))
# a= X * (0.6) 
# b= y * (0.4)
# sonuc=(a+b) / 2
# print(f" notunuz: {sonuc} , dersten geçme durumunuz: {sonuc >= 50}")


#PAROLA VE EMAİL BİLGİSİİ İSTEYİP DOĞRULUĞUNU KONTROL EDİN
#EMAİL= EMAİL@SAKIDTURAN.COM PAROLA:ABC123

# mail= "EMAİL@SAKIDTURAN.COM"
# parola= "ABC123"
# x=input("lütfen mailinizi girin:")
# y=input("lütfen şifrenizi girin:")
# sal= (mail == x)
# kal= ( parola == y)
# print(f"mail doğru mu: {sal},parola doğru mu:{kal}")

#GİRİLEN BİR SAYINN POZİTİF ÇİFT SAYI OLUP OLMADIĞINI KONTROL EDİNİZ.
# x=int(input("sayı:"))
# kontrol= (x > 0) and (x % 2 == 0)
# print(kontrol)

#FARKLI BİR KONU
# x=[1,2,3]
# y=[2,4]
#del x[2]  #2 değeri endeks bilgisidir
#print(x)
# y[1]= 1
# print(y)

#İN BAĞLACI
# x=["apple","banana"]
# print("banana" in x)

