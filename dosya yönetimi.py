# "w": (write) yazma modu.dosya oluşturma.yazarken direkt içindekini siler ve yeni gönderiyi yazar
# file=open("newfile.txt","w")
# file.close()

# file=open("newfile","w",encoding="utf-8")
# file.write("sadık turan naber")
# file.close()

# "a": (append) ekleme.mevcut yazının üzerine ekler
# file=open("newfile","a",encoding="utf-8")
# file.write("sadıkturan\n")
# file.close()

#  "x": (create) oluşturma.direk sadece dosya oluşturur
#  file=open("newfile2","x",encoding="utf-8")

# "r": (read)   okuma
# file=open("newfile","r",encoding="utf-8")
# kal=file.read()
# print(kal)
# file.close()

# file=open("newfile","r",encoding="utf-8")
# kal=file.read(5)
# print(kal)
# file.close()

# file=open("newfile","r",encoding="utf-8")
# kal=file.readline()
# print(kal)
# file.close()
################################################

#normalde her dosya açtığımızda yani open() dan sonra file.close diyorduk
#ama bunun yerine (with) komudunu kullanabiliriz 

# with open("newfile","r",encoding="utf-8") as file:
#     kal=file.read()
#     print(kal)
##################################################

# dosyada başındaki cümlenin yerine bir şey yazdırmak istediğimizde veya özellikle belli bir konuma bir şey yazdırmak istediğimizde r+ ile yazarız
# ama direkt dostanın sonuna bir şey eklemek istiyorsan a ile direkt yazabilirsin
 
# with open("niwfile.txt","w",encoding="utf8") as file:
#     file.write("ahmet çakar\nyunus akgün\nmuslera")
# with open("niwfile.txt","r",encoding="utf8") as file:
#     print(file.read())

# with open("niwfile.txt","a",encoding="utf-8") as file: 
#     file.write("\nkenan ışık\nkenan yıldız")
# with open("niwfile.txt","r",encoding="utf-8") as file:
#       print(file.read())

# with open("niwfile.txt","r+",encoding="utf-8") as file:
#     file.write("kenan ışık")
########################################################
# ÖRNEK  

# def hesap(gelen):
#     gelen=gelen.strip()
#     liste=gelen.split(":")
#     adsoyad=liste[0]
#     notlar=liste[1].split(",")
#     notlar=[int(n)for n in notlar]
#     ortalama= sum(notlar)/len(notlar)
#     if ortalama >=90 and ortalama<=100:
#          harf="AA"
#     elif ortalama>=85 and ortalama<=89:
#          harf="BA"
#     elif ortalama>=65 and ortalama<=84:
#          harf="CC"
#     else:
#          harf="FF"
#     return f"{adsoyad}: ortalama{ortalama:.2f}({harf})"
# def notları_gör():
#     with open("dosya.txt","r",encoding="utf-8") as file:
#         for f in file:
#             print(hesap(f))
# def not_gir():
#     ad=input("ad:")
#     soyad=input("soyad:")
#     not1=input("not1:")
#     not2=input("not2:")
#     not3=input("not3:")
#     with open("dosya.txt","a",encoding="utf-8") as file:
#         file.write(f"{ad} {soyad} : {not1},{not2},{not3}\n")        
# def kayıt():
#     with open("dosya.txt","r",encoding="utf-8") as file:
#         liste=[]
#         for x in file:
#             liste.append(hesap(x))
#     with open("notlar.txt","w",encoding="utf-8") as file2:
#         for i in liste:
#           file2.write(f"{i}\n")
                      
# while True:
#     islem=input("1-notlar\n2-not gir\n3-notları kayıt et\n4-çık\n")
#     if islem == "1":
#         notları_gör()
#     elif islem == "2":
#         not_gir()
#     elif islem == "3":
#         kayıt()
#     else:
#         break

    

