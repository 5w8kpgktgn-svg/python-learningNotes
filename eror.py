# try:
#     x=int(input("x:"))
#     y=int(input("y:"))
#     print(x/y)
# except:
#     print("yanlış bilgi girdiniz")

##########################################
# try:
#     x=int(input("x:"))
#     y=int(input("y:"))
#     print(x/y)

# except Exception as ex:
#     print("yanlış bilgi girdiniz",ex)

##########################################
# while True:
#   try:
#      x=int(input("x:"))
#      y=int(input("y:"))
#      print(x/y)
#   except:
#     print("yanlış bilgi girdiniz")
#   else:
#      break
# print("test bitti...")
  
###########################################

# while True:
#     try:
#       x=int(input("x:"))
#       y=int(input("y:"))
#       print(x/y)
#     except:
#      print("yanlış bilgi girdiniz")
#     else:
#       break
#     finally:                       #finally kısmı ne olursa olsun çalışır
#       print("tebrikler")
# print("test bitti...")

###########################################
# kendi hata kodumuzu oluşturma (parola oluşturma)

# def parola(psw):
#      import re         #re.search() bir tür bizim belirlediğimiz değerde arama motorudur.tabi önce import re olarak açmamız gerekir
#      if len(psw) < 8:
#          raise Exception ("parola en az 7 karakter olmalıdır")
#      elif not re.search("[a-z]",psw):
#          raise Exception ("parolada küçük harf olmalıdır")
#      elif not re.search("[A-Z]",psw):
#          raise Exception ("büyük harf içermelidir")
#      elif not re.search("[0-9]",psw):
#          raise Exception ("rakam içermelidir")
#      elif re.search("\s",psw):
#          raise Exception ("boşluk içermemelidir")
#      else:
#          print("başarılı bir şekilde parola oluşturuldu")
         
    
# pasword="12345678aA"
# try:
#      parola(pasword)
# except Exception as ex:
#     print(ex)

    
##############################################

# class person:
#     def __init__(self,name,year):
#         if len(name) > 10:
#             raise Exception ("name alanı 10 dan fazla karakret içermemelidir")
#         else:
#             self.name=name
#             self.year=year
# p=person("aliiiiiiiiiiiiiiiiiiiiii",1990)
# print(p)
    
################################################
#(parola oluşturma ama while da var)

# def parola(şifre):

#      import re
#      if len(şifre) < 8:
#          raise Exception ("şifre en az 8 karakter olmalıdır")
#      elif not re.search("[a-z]",şifre):
#          raise Exception ("şifrede küçük harf bulunmalıdır")
#      elif not re.search("[A-Z]",şifre):
#          raise Exception("şifrede büyük harf bulunmalıdır")
#      elif not re.search("[0-9]",şifre):
#          raise Exception ("şifrede rakam olmalıdır")
#      elif re.search("[\s]",şifre):
#          raise Exception ("şifrede boşluk olmamalıdır")
    
# while True:
#   kilit=input("parola:")

#   try:
#      parola(kilit)
#   except Exception as ex:
#      print(ex)
#   else:
#      print("parola başarılı bir şekilde oluşturuldu")
#      break
######################################################
#örnekler

liste=["1","2","5a","10b","abc","10","50"]
#1-liste elemanları içindeki sayısal değerleri bulunuz.
# for g in liste:
#     try:
#         kal=int(g)
#         print(kal)
#     except:
#         continue
   

#2- kullanıcı "q" değerini girmedikçe aldığınız her inputun sayı
#olduğundan emin olunuz aksi halde hata mesajı yazınız
# while True:
#     kal=input("sayı gir:")
#     if kal == "q":
#         break
#     try:
#       değer=float(kal)
#       print(değer)
#     except Exception as ex:
#       print("lütfen bir sayı girin")

#3- girilen parola içinde türkçe karakter hatası veriniz
# def parola(şifre):
#     import re
#     if re.search("[ğ, Ğ, ç, Ç, ş, Ş, ü, Ü, ö, Ö, ı, İ]",şifre):
#         raise Exception("lütfen türkçe karakter kullanmayın")
# while True:
#   kal=input("şifre oluştur:")
#   try:
#     parola(kal)
#   except Exception as ex:
#     print(ex)
#   else:
#      print("şifreniz başarılı bir şekilde oluşturuldu")
#      break
#4-faktöriyel fonkdiyonu oluşturup fonksiyona gelen değer için hata mesajları verin
def faktöriyel(x):
    x=int(x)
    if x <= 0:
        raise Exception ("negatif veya sıfır değeri")
    değer=1
    for i in range(1,x+1):
        değer *=i
    print(değer)

try:
    for x in [5,10,20,-3,"10a"]:
     faktöriyel(x)
except Exception as ex:
    print(ex)

