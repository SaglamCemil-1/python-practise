#set
# küme -> aynı eleman yok

houses = set()
houses.add("a")
print(houses)

#global-local
#localler diğer fonksiyonlara aktarılamaz

balance = 0
def bank_balance()->bool:
    print("Balance:",balance)
    return 0

def deposit(d):
    global balance
    balance += d

def withdraw(w):
    global balance 
    balance -=w

#constant -> değişmeyen
#class yapıp içine sallayıp kullanılmalı:

class Cat:
    meow = 5

    def cat_meows(self) -> None:
        for _ in range(Cat.meow):
            print("meow")

cat = Cat()
cat.cat_meows()


#mypy -> lib değil , çalışma şekli -> mypy code.py
# type hints çalışıyormu bakar

#get_num : int = int(input("")) 

                    #docstrings
                    #how to document function

def numerous_print(n:int) -> str:
    """ 
    I have no freaking idea about this function
    
    :param n:Number of times
    :type n:int
    :raise TypeError: if n is not int
    :return A string
    :rtype: str

    """
    return "meow\n"*n

print(numerous_print(3),end ="") 


                #argparse lib ?!

                #UNPACKİNG

firs,last = input("wht ? ").split(" ")
print(f"{firs} {last}")

""" YERİNE ||| unpacking kullanılır"""

def toplama(arg1,arg2,arg3):
    return (arg1*arg2+arg3)

arguments = [1,2,3]
print(toplama(*arguments) , "dir")


def verileri_yazdir(*args, **kwargs):
    print("Pozisyonel:", args) # Tuple döner
    print("İsimlendirilmiş:", kwargs) # Dict döner

#verileri_yazdir(x=a,y=b) şeklinde **kwargs agönderilir
#verileri_yazdir({x:a,y:b}) -> yanlış
"""
--> burdada olduğu gibi **keyword *arguman şeklinde (*)
döner yani dict atıldığında -> ** olmalı keyleri dönsün
"""

arguments__ = {"arg1":7,"arg2":3,"arg3":4}
print(toplama(**arguments__),"dir")

#for x,y in herhangibirdict.items() -> key value
#for x,y in tuple -> i(döngü sırası),y = tuple elemanıs

############ MAP -> fonksiyona bp gösterme

def main():
    yell("this"," is ","cs50p","aaa")

def yell(*words):
    """
    uppercased = list()
    for word in words:
        uppercased.append(word.upper())
    """
    #uppercased = map(str.upper,words) 
    uppercased = [word.upper() for word in words]
    print(*uppercased,end="") #unpacking

main()


### List comprehensions-> yell(-uppercased) +

students = [
    {"name":"Cemil","house":"Trabzon"},
    {"name":"Arda","house":"Trabzon"},
    {"name":"Ali","house":"Trabzon"},
    {"name":"CAN","house":"Trabzon"},
]

Trabzonlular = [
    student["name"] for student in students if student["name"] == "Trabzon"
]
for trabzon in Trabzonlular:
    print(trabzon)

    #####    FİLTER    ##### 

def is_trabzon(s):
    return s["house"] == "Trabzon"

Trabzonlular = filter(is_trabzon,students)
### --- filter(lambda s: s["house"]=="Trabzon",students)

for trabzon in Trabzonlular: #sorted(Trabzonlular)
    print(Trabzonlular["name"])


    ##### DİCT comprehensions #####
students = ["Alican","Arda","Cemil"]

Trabzonlular = [
{"name":student,"house":"Trabzon"} for student in students
]

#liste dict lerle dolu ama 1 tane büyük dict döndürülecekse:
students = ["Alican","Arda","Cemil"]
Trabzonlular = {student :"Trabzon" for student in students}



    ### ENUMERATE (iterable,start = 0) ###

students = ["Alican","Arda","Cemil"]

for i,student in enumerate(students):
    print(i+1,students)


####    GENERATORS /     İTERATORS /      YİELD     ####

#   docs.python.org/3/howto/functional.html#generators

## yield -- return 

def sheep(n):
    for i in range(n):
        yield "A"*i

def main():
    n = input("A: ")
    for s in sheep(n):
        print(n)