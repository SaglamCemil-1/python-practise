
class get_student_informations:
    def __init__(self,name,house):
        if not name :
            raise ValueError("name is not initialize")
        #name değişkeni atanmamışsa value error
        if house not in ["balububalubu"]:
            raise ValueError("wrong house")
        #initialize 
        #obje öğreleri atama
        self.name = name
        self.house = house

        #öğrenci bilgisi override edilmesin diye: setter/getter
        @property
        def house(self):
            return self._house

        @property
        def name(self):
            self._name

        @name.setter
        def name(self,name):
            if ["a"] in name:
                raise ValueError("name cannot contain 'a' ")
            if not name:
                raise ValueError("there is no name")
            self._name = name
        #_ house() ile self.house karışmasın diye
        #self.house setter i tetikelr self._house lar tetikelemez
        #self.değişken kullanılırsa setter çalışır.
        @house.setter
        def house(self,house):
            #getter
            if house not in ["balububalubu"]:
                raise ValueError("balubu")
            self._house = house

        @classmethod
        def class_method(cls):
            name = input("name:")
            house = input("house:")
            return cls(name,house)
        
"""
cls ile __init__ farkı class içinde x = yyy şeklinde değişken 
varken classnamelowecase = classname (objeye dönmesi için) oluşturmak
gerekmez çünkü veri zaten otomatik class da var olur ama __init__ de 
constructor class atanmalı ki oluşmalı sounç:

__init__ / self
class = Class()
class.method("vaeiable")

@classmethod / cls
Class.method()
"""
        
        



def main():
    student = get_student_informations.class_method()
    print(f"{student["name"]} is from {student["house"]}")

"""
def get_student():
    student = {}
    student["name"] = input("name :")
    student["house"] = input("house :")

    return student
    #return {home: x , name:y} yapsaydım ilk satıra gerek yoktu
"""


def get_that_shit():
    shit = get_student_informations()
    # burda shit artık bir class / nesne 
    # attribitu göndermek için 

    #f stringe dönüldümü -> shit["key"] ---- >  shit.key olur
    shit.name = input("shit : ")
    shit.house = input("shit : ")
    #yada shit = get_student_informations(name , house) da olur
    #bu nun içinde artık name değişkeni ve inputun değeri var.



    """         İNHERİTANCE             """

class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("miss")
        self.name = name
# super() ->superclass
#x(Wizard) -> x class ı wizardı superclass alıyor
#supr().__init__() -> superclass tan init fonksiyonu
class Student(Wizard):
    def __init__(self, name,house):
        super().__init__(name)
        self.house = house

class Proffesors(Wizard):
    def __init__(self, name , house):
        super().__init__(name)
        self.house = house


        """         OPERTATOR OVERLOADİNG           """
        # - işareti illaki çıkarma olmak zorunda değil (örn)

# __add__(self,other)
#   x = self.x + other.x 
# self bizim ilk object imiz , other 2.object imiz 
#2 class toplamını buldurur