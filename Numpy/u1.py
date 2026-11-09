#%%
import numpy as np

i,y = 4,4
L = np.empty((i,y))
for _ in range(i):
    for t in range(y):
        L[_][t] = np.random.random()

#print("A:" ,np.random.random((1,1)))
print("------------NDİM/SHAPE/TYPE-----------")
print(L)
print(type(L),end=" ")
print("dimension:",L.ndim,"shape:",end=" ") 
#number of dimension
print(L.shape)
print("--------------------------------------")

#print(np.ones((2,2,2,2),dtype="int"))
print(L)
for i in L[0:2]:
    print(i[0:2],end="")
print("\n")
print("-------------SLICING------------------")
print(L[0:2,0:2])
print(L[:,2]) #sütun seçimi
print(L[2,:]) #satır seçimi

"""  L[0][0][0] = L[0,0,0] """
"""  L[0:2] gibi atamalar yeni array oluşturur
-> L[0:2][0:2][0:2] = L[0:2]
-> (doğrusu) L[0:2,0:2,0:2]
"""
print("-----------SCALAR ARITHMETIC----------")
print(L + 1)
print("-------  VECTORİZED MATH FUNC  -------")
print(np.sqrt(L))
r1,r2,r3 = 1,2,3 #alanlarını hesaplayalım
print("-----------EXERCISE-------------------")
def main_sequence(_list:list):
    new_list = []
    for i in _list:
        new_list.append(i*i*np.pi)
    return new_list

print(list(map(lambda x:round(x,2),main_sequence([r1,r2,r3]))))
"""--- yada ---"""
half = np.array([1,2,3])
half2= np.array([2,3,4])
print(half ** 2 * np.pi)
print("--------ELEMENT WISE ARITHMETIC-------")
print(half2 + half, half ** half2) #topla-çıkar-çarp-böl


"""-------------        önemli      ----------------"""
print("--------COMPARISON OPERATORS----------")
scores = np.array([20,70,100,52,74,68])
scores[scores<50] = 0
print(scores)

#33:34 BROCODE
print("---------------BROADCASTİNG-----------")
# biri 1 olcak yada eşit olcaklar

array_1_ = np.array([[1,2,3,4]])
array_2_ = np.array([[1],[2],[3],[4]])

print(array_1_.shape,"-",array_2_.shape)
#shape 4,1 1,4 eğer 1ler yerine başka sayı olsaydı çalışmaz
# 4,4 1,4 olur 4,4 4,4 olur
print(array_1_,array_2_,sep="\n")

print(array_1_ * array_2_)
#same -> print(array_2_ * array_1_)

"""example"""

multiple_1 = np.array([[x for x in range(1,11)]])
multiple_2 = np.array([
    [1],[2],[3],[4],[5],[6],[7],[8],[9],[10]
    ])

print(multiple_1 * multiple_2)
print("---------------AGGREGATE FUNCTIONS -----------")
#summarize data - return single value

aggre = np.array([[1,13],[17,7]])
print(aggre,"sum:",np.sum(aggre))
print(aggre,"sum:",np.sum(aggre,axis=0)) 
#tüm sutünları toplar  13+1 , 17+7
print(aggre,"sum:",np.sum(aggre,axis=1))
#tüm satırları toplar 1+17 , 13+7
print(aggre,"sum/elements:",np.mean(aggre))
print(aggre,"std:",np.std(aggre))
print(aggre,":",np.var(aggre))
print(aggre,":",np.min(aggre))
print(aggre,":",np.max(aggre))
print(aggre,":",np.argmin(aggre)) #pozition minvalue
print(aggre,":",np.argmax(aggre)) # 0-> 1 ,1->13 ,2->17

print("---------------FILTERING-----------")
ages = np.array([
                 [21,17,19,20,16,30,18,65],
                 [39,22,15,99,18,19,20,21]
                ])

teenagers = ages[ages<18] #one dimensional
adults = ages[(ages>=18) & (ages<=65)] #and çalışmaz
# new array = array[python expression]
print(teenagers)
#shape i korumak için
where = np.where(ages >=18,ages,0) 
    #condition , arrayname , fill value 
print(where)
print("---------------RANDOM NUMBERS-----------")

rng = np.random.default_rng(seed=1)
print(rng.integers(1,100,size=(4,4)))

np.random.seed(seed=1)
print(np.random.uniform(1,100,size=(2,3)))

#shuffling
rng = np.random.default_rng()
array = np.array([1,2,3,4])
rng.shuffle(array)
print(rng.choice(array,size=(2,2)))
print(array)

"""exercise"""

random_emojies = np.array([
["😀", "🎉", "🚀", "🔥", "🐱", "🌟", "💡", "🍕", "🎈", "🍀"]
])
rng = np.random.default_rng()
print(random_emojies)
print(rng.choice(random_emojies,size=(1,1)))

print("---------------RESHAPING ARRAYS-----------")

re_array = np.arange(1,10).reshape((3,3))
array1 = np.array([1,2,3])
array1.reshape((1,3))
print(array1)
#reshape -- newaxis
array1[np.newaxis,:]
print(array1)
array1.reshape((3,1))
print(array1)
array1[:,np.newaxis]

print("-----------ARRAY BÖL/BİRLEŞTİR-ME---------")

#2D -> alt alta , 1D -> Yan yana

#birleştir -> concatenation

x = np.array([1,2,3])
y = np.array([3,2,1])

print(np.concatenate([x,y]))
print(np.concatenate([y,x]))
#birden fazla aynı anda birleştirilebilir

grid = np.array([[1,2,3],
                 [4,5,6]])
print(np.concatenate([grid,grid],axis=0))
#yan yana için axis=1

#karışık dimension için : (1D-2D falan)
print(np.vstack([x,grid]))
#vertically - horizontally stack --- h/v stack
y = np.array([[99],[99]])
print(np.hstack([grid,y])) #-> sona ekledi
#dstack

print("-----------------SPLİT-------------")
#shift + enter ile çalıştır

big_array = [1,2,3,4,5,4,3,2,1]
x1,x2,x3 = np.split(big_array,[3,6]) #3,5. endekslerde kes
print(x1,x2,x3)

hsplitter = np.array([[1,2,3,4],
                      [5,6,7,8],
                      [9,10,11,12],
                      [13,14,15,16],
                    ])

print(np.hsplit(hsplitter,[2]),sep="\n")
print(np.vsplit(hsplitter,[2]),sep="\n")

print("-------- Comparison OP -----------")

arr = np.arange(16).reshape(4,4)
print(arr < 3)

print(np.count_nonzero(arr < 7)) 
#yada sum, sum satır sütün bölünerek uygulanabilir
print(np.sum(arr<6,axis=1)) 
#ilk satır 4 2satır 2 sonraları 0
print(np.any(arr < 4,axis=1))
#np.any , np.all

print("---------FANCY INDEXING ---------------")
X = np.arange(12).reshape((3, 4))

row = np.array([0, 1, 2])
col = np.array([2, 1, 3])
X[row[:,np.newaxis], col] #-> row[0],col[0] row[1],col[1]

array_X = np.arange(10)
ch = row
print(array_X)
array_X[ch] = 99 #0,1,2 ncü elementler oldu 99
print(array_X)
array_X[ch] -=15
print(array_X)
#add.at(x,y,addvalue) -> reduce.at(x,y,reduceVal)

np.random.seed(42)
print(np.histogram(np.random.randn(100), bins=np.linspace(-5, 5, 20))[0])
#bins -> kutu oluşturan
#histogram(X,y) x-> dağıtılcak eleman

"""
histogram([1,2,3,1.2,0.7],bins=[0,1,2,3])
0-1 , 1-2 , 2-3 3 kutu oluştu 
1,2,3 ü dağıtmalıyız -- 1-> 1-2 , 2-> 2, 3->2-3 (son kutu son eleman dahildir)
1.2 --> 1-2 , 0.7 --> 0-1 yani 0-1 de 1 sayı 1-2 de 2 tane 2-3 te 2 tane oldu
return -> [1,2,2]
"""

#python fonksiyon yavaşlığından kaynaklı loop oluşturulmamalı.
"""
+	np.add	Addition (e.g., 1 + 1 = 2)
-	np.subtract	Subtraction (e.g., 3 - 2 = 1)
-	np.negative	Unary negation (e.g., -2)
*	np.multiply	Multiplication (e.g., 2 * 3 = 6)
/	np.divide	Division (e.g., 3 / 2 = 1.5)
//	np.floor_divide	Floor division (e.g., 3 // 2 = 1)
**	np.power	Exponentiation (e.g., 2 ** 3 = 8)
%	np.mod	Modulus/remainder (e.g., 9 % 4 = 1)
"""

x7 = [1,2,3]
print("2 ** x = ",np.exp2(x))
print("e ** x = ",np.exp(x)) #+ np.log(x)

y=np.empty(3)
np.multiply(x7,5,out=y)
print(y)

#npempty -> boş dizi / çarpıp elemanları ona yerleştirdi

#Sorting arrays -> algoritma
#broadcasting -> boyut genişletme

#structured data (aşşağıda)    
data = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
                          'formats':('U10', 'i4', 'f8')})
print(data.dtype)

#düz liste gibi çağrılıp kullanılır 
name = ['Alice', 'Bob', 'Cathy', 'Doug']
age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]

data['name'] = name
data['age'] = age
data['weight'] = weight

print(data[data['age']<30]) #yaşı 30 altında olanlar

## elemanlar eşit aralıklı değilse memory kopyalar
# eşit aralıklı ise üste yazar
