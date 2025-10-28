# YÖNTEM 1
# import math
# değer=math.sqrt(49)
# print(değer)
###################################################
# YÖNTEM 2
# from math import*  # bu math modülünden tüm kütüpaneleri değerlerin al demek
# from math import factorial,sqrt,ceil  # burda ise math modülünden sadece bizim tanıttığımız kütüpaneleri kullanabilir
# from math import*
# değer= factorial(5)
# print(değer)
###################################################
# listeden randon veri çekmek
# import random
# names=["ali","yağmur","deniz","cenk"]
# değer=names[random.randint(0,len(names)-1)]
# print(değer)
      # or
# import random
# names=["ali","yağmur","deniz","cenk"]                     #burda amaç random içinde böyle komutlar var diye bilmek,ezbere gerek yok bunlar zaten internette yazıyor
# değer=random.choice(names)
# print(değer)
#####################################################
# listeyi karıştırmak
# import random
# liste=list(range(20))
# random.shuffle(liste)
# print(liste)
#####################################################
# liste içinden rastgele 3 sayı al
# import random
# liste=range(100)
# değer=random.sample(liste,3)
# print(değer)
#####################################################

