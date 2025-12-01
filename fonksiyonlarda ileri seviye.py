# GİZLİ TUTULAN FONKSİYON(iç içe fonksiyon)

# faktöriyel

# def factorial(number):
#     def inner_factorial(number):
#         if number <=1:
#             return 1
#         return number * inner_factorial(number - 1)
#     return inner_factorial(number)
# print(factorial(5))          #burada inner factorial a direk ulaşamıyoruz ,factorial yardımıyla ona ulaşabiliriz
                             # faktöriyelin çalışma mantığı ise şöyle 5 girdiğinde inner_factorial(4) çalışıyor bu da 4*inner_factorial(3) bu da 3 ü çağıtıyor en son 1 oldumu 1 olrak dönüyor ve çarpma yapılmış oluyor

################################################################
# FONKSİYONUN ALT FONKSİYONLARINA İŞLEM YAPTIRMA

# ÖRNEK1
# def usalma(number):
#     def inner(power):
#         return number ** power
#     return inner
# two=usalma(2)
# three=usalma(3)
# print(two(4))
# print(three(5))

# ÖRNEK2
# def yetki_sorgula(page):
#     def inner(role):
#         if role == "admin":
#             return "{0} rolü {1} sayfasına ulaşabilir".format(role,page)
#         else:
#             return f"{role} rolü {page} sayfasına ulaşamaz"
#     return inner
# user1=yetki_sorgula("product edit")
# user2=yetki_sorgula("product edit")
# print(user1("admin"))
# print(user2("müşteri"))

# ÖRNEK3

# def islem(islem_adi):
#     def toplama_islemi(*args):
#         toplam=0
#         for i in args:
#             toplam+=i
#         return toplam
#     def çarpma_islemi(*args):
#         çarpma=1
#         for x in args:
#             çarpma*=x
#         return çarpma
#     if islem_adi == "toplama":
#         return toplama_islemi
#     else:
#         return çarpma_islemi

# görev1=islem("toplama")
# print(görev1(1,3,5,7))
# görev2=islem("çarpma")
# print(görev2(1,3,5,7))

#######################################################
# DECORATOR (YANİ BİR FONKSİYONU BAŞKA BİR FONKSİYONA ATARAK ÖNCESİNİ SONRASONI SÜSLEMEK)

# def my_decorator(func):
#     def wrapper(name):
#         print("fonkisyndan önceki işlemler")
#         func(name)
#         print("fonksiyondan sonraki işlemler")
#     return wrapper
# @my_decorator
# def sayHello(name):
#     print("hello",name)
# sayHello("ali")

# ÖRNEK1

# def sutlu_devorator(fonksiyon):
#     def kal():
#         return fonksiyon() + " + süt"
#     return kal
# @sutlu_devorator
# def kahve():
#     return "sade kahve"
# print(kahve())

# ÖRNEK2

# import time
# def zaman_olcer(fonksiyon):
#     def kal(*args,**kwargs):       #*args,**kwargs ilede fonkisyona ne gönderirsen veya kaç tane gönderirsek çalışsın diye bunları giriyoruz
#         basla=time.time()
#         sonuc= fonksiyon(*args, **kwargs)    #sonuc aşaması önce ve sora zaman aralığına alarak sayana kadarki süreyi ölçüyoruz
#         bitis=time.time()
#         print(f"{fonksiyon.__name__} {bitis - basla:.3f} saniyede çalıştı")
#         return sonuc
#     return kal
# @zaman_olcer
# def say():
#     for i in range(1000000):
#         pass
# say()

# ÖRNEK3

# import math
# import time
# def zaman_olcer(func):
#     def kal(*args,**kwargs):
#         start=time.time()
#         func(*args,**kwargs)
#         finish=time.time()
#         print(f"fonksiyon {func.__name__} {finish-start} sürede tamamlandı")
#     return kal
# @zaman_olcer
# def usalma(a,b):
#     print(math.pow(a,b))
# @zaman_olcer
# def faktoriyerl(num):
#     print(math.factorial(num))
# usalma(2,3)
# faktoriyerl(5)
