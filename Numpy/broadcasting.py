            # BROADCASTING #

import numpy as np

new_array = np.random.random((10,4))
reshaped_1 = new_array.reshape(8,5).mean(0)

sec_array = np.arange(5)
reshaped_2 = sec_array.reshape(1,5).mean(0)

print(reshaped_1)
print(reshaped_2)

print("-------------------")
try:
    print(reshaped_1 + reshaped_2)
except:
    print("err:")

new_array = new_array.reshape((8,5))
sec_array = sec_array.reshape((1,5))

print("-------------------")
print(
    new_array.mean(1),
    "\n",
    sec_array.mean(1),
    "\n",
    new_array.mean(1)+sec_array.mean(1),
    "\n"
    )
# print(new_array + sec_array)

print("----- STRUCTURED ARRAYS ----")
    # STRUCTURED ARRAYS # 

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

print(data[data['age']<30]['name']) #yaşı 30 altında olanlar 

"""
Character	Description	            Example
'b'	        Byte	                np.dtype('b')
'i'	        Signed integer	        np.dtype('i4') == np.int32
'u'	        Unsigned integer        np.dtype('u1') == np.uint8
'f'	        Floating point	        np.dtype('f8') == np.int64
'c'	        Complex floating point	np.dtype('c16') == np.complex128
'S', 'a'	String	np.dtype('S5')
'U'	        Unicode string	        np.dtype('U') == np.str_
'V'	        Raw data (void)	        np.dtype('V') == np.void
"""

