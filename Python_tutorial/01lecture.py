""" 

user_input = input("sentence: ")
print(user_input   , user_input )
print(f"{user_input}")

user_input = user_input.strip().title() 
# sonsuz sayıda fonksiyon ardı ardına kullanılabilir,

first, last = user_input.split(" ") 
#bölünmüş [1] = ilk [2]= 2.    #örn : Abd USS -> first= Abd last =USS

print(user_input)

#herhangi bir dilde kodu açıklama ->pseudocode    # escaping -> \
print(round(250.1554223554125541122543,12))

big_number = 100000000 #sistemin 3sıfırdan bölmesiin sağlamak için
print(f"{big_number:,}")
# print(f"{sayı:.2f}")-> 2 tane basamağa yuvarladık -alternatif- round(sayı,2)
 
def greetings(user_input="alallalalal"): #define -> fonksiyon oluşturmak 
    return user_input + "hello"
print(greetings(user_input))
print(greetings())


                                #if 

x = 75 #userinput
#alternatif 1 [optimize]
if x>=100:
    print("bu 100den büyükse çalışır ve aşşağı inmez")
elif x>=80:
    print("bu sadece 80den büyükse çalışır ve aşşağı inmez (eğer büyükse)")
elif x>=60:
    print("bu 60 dan büyük olursa sadece çalışır")

#alternatif 2
if 100 < x:
    print("bu 100den büyükse çalışır ve aşşağı inmez")
elif 80 <= x < 100:
    print("bu sadece 80den büyükse çalışır ve aşşağı inmez (eğer büyükse)")
elif 60 <= x < 80:
    print("bu 60 dan büyük olursa sadece çalışır")

#shorthand
def shorthand(x):
    return True if x %2 == 0 else False
    # okunabilir alternatif [2] --->  return x %2 == 0

                                #match
name = input("name") 
match name:
    case "X" | "XX" | "XXX":                # | = or #
        print("x")
    case "Y":
        print("Y")
    case "Z":
        print("Z")
    case _:
        print("else gibi çalışır")

                                #FOR

#for için arttırmaya gerek yok 
for _ in range(15):
    print("black mamba")
#otomatik olarak i yi arttıracak


                                #while

#aynı
i = 0
while i <=10:
    print("mamba")
    i += 1

                                #pythonic type

print (" meow \n " * 3, end = "") #default / i override ettik boşluk bırakmasın diye

                                #input validation

n = -1
while n < 0 :
    n = int(input(" N ?"))
    print("meow \n" * n, end = "")

while True:
    c = int(input("What is C ? "))
    if c > 0:
        print("meow \n" * c , end = "")
        break
    print("aaa")

                                #Dict
-------------------------------------------------------------
DİCTİONARY OLUŞTURMA

x = {"a": değişken1, "b": değişken2}

x2 = {"a": değişken1}
x2= {"b" : değişken2}

x3 = dict(zip(değişken1,değişken2))

meyveler = dict(elma=10, muz=20, cilek=30)

ciftler = [("A", 1), ("B", 2), ("C", 3)]
sozluk = dict(ciftler)
*
Gelişmiş dict 

kareler = {x: x**2 for x in range(1, 5)}

isimler = ["Ali", "Veli"]
indeksli = {indeks: isim for indeks, isim in enumerate(isimler)}

gelişmiş dict
*
anahtarlar = ["sunucu1", "sunucu2", "sunucu3"]
sistemler = dict.fromkeys(anahtarlar, "Aktif")
-----------------------------------------------------------
abkeys = ["a","b","c"]
abvalues = ["a1","b2","c3"]

abdict = {"a":"a1","b":"b2","c":"c3",}
print(abdict["a"])

for student in abdict:
    print(student,abdict[student])  #keyleri gönderecek , sadece valueleri döndürecek


                                #TRY-EXCEPT

try: 
    x=int(input("integer?: "))
    print(f"x is {x}")
except ValueError:
    print("x isnot an integer")
# en iyi yöntem try: kısmında bir yada çok az satır kod dönmesidir print bloğu
# en alta (exceptten altta intendationsuz yazmaktır) -> nameerror döner bu sefer

try: 
    x = int(input("x =?: "))
except ValueError:
    print("valueeror")
#value error dönünce atama yapılmadı - nameerror döner x var olmadığı için, 
else: 
    print(f"x is {x}")

                                # sürekli yapmak

while True:
    try: 
        x = int(input("x =?: "))
    except ValueError:
        print("valueeror")
    else: 
        break
        
print(f"x is {x}")

def get_int():
    while True:
        try: 
            x = int(input("x =?: ")) #eğer hata görürse hemen except e iner
        except ValueError:
            print("valueeror")
            #pass de gelebilir erroru atlarız
        else: 
            break   #gerek yok return u buraya yazabilirdik
    return x
        
print(f"x is {x}")

                                    #Random
import random
# import random import choice: random.choice() -> choice

tura = 0
yazı = 0
for i in range(100):
    coin = random.choice(["tura","yazı"])
    if coin == "tura":
        tura += 1
    else:
        yazı += 1

print(f"yazı sayısı: {yazı/100}")
print(f"tura sayısı {tura/100}")
print(f"tura yazı oranı {tura/yazı}")

                                    #SYS
import  sys
#çoklu argüman sys.argv
print("hello my name is ", sys.argv[1]) #arg[0] = 01lecture.py  ->    proje ismi
try:
    print("hello my name is: " + sys.argv[1])
except IndexError:
    print("hello my name is " + "default")

#conditionals-> if len(sys.argv[2])<2 

                                    #sysexit 

if len(sys.argv) <2:
    sys.exit("too few")
elif len(sys.argv)>2:
    sys.exit("too much")
print("hello , my name is " , sys.argv[1])

#birden fazla eleman 
for arg in sys.argv:
    if arg == sys.argv[0]:
        continue
    print("hello my name is " + arg)
   
                                #SLİCİNG

mylist = ["apples","bananas","gorilla","mammoot","IDK","1",3]

for argument in mylist[1:]:     #1 den sonrakiler (1 dahil)
    print(argument, end=" / ")

for argument in mylist[1:2:1]:  #1 den 2 ye kadar "sadece 1"
    print(argument, end=" & ")  

for argument in mylist[3:0:-1]: # 3 ten 0 geri doğru
    print(argument, end=" | ")

# packages / pypiorg / pip -> lib download

                                #cowsay

import cowsay

cowsay.trex("hello Cemil")

                                #requests
""" 
import json
import requests
import sys
if len(sys.argv) != 2: #veri 1 , veri 2
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+ sys.argv[1])
print(response.json())
#python 01lecture.py weezer

responsejson = response.json()
for responses in responsejson["results"]:
    print("Sanatçı:", responses["artistName"])
    print("Şarkı:", responses["trackName"])
    print("Albüm:", responses["collectionName"])
    print("-" * 30)

print(json.dumps(response.json(), indent=2))

o = response.json()


def main():
    print("hello")
if __name__ == "__main__":
    main()  #eğer bu dosya main olarak çalıştırılmış (run a basılmış) ise çalışır

        #assert -> verilen koşul true + false ise error döner
        #assert hata verdimi durdurup yazar alt satırlar çalışmaz
        #test dosyası oluşturrken packages !!! __init__.py !!

                        # UNİT TEST

        #PACKAGES NEDİR ??
        #packages testlerinde python -m pytest test_calculator.py yerine python -m pytest foldername