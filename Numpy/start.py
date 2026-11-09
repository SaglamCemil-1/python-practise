import numpy as np

shape = input("shape: ") # 3,3,3
rule = input("rule (<,>,=): ")
rule_int = float(input("floating point: "))

shape_i = shape.split(',')
i = 1
for _ in range(len(shape_i)):
    i *= int(shape_i[_])

shape_i = [int (x) for(x) in shape_i]
new_array = np.random.random(([int(x) for x in shape_i])) #dahili
new_array_copy = new_array.reshape(*shape_i)

match rule:
    case ">":
        rule_array = np.where(  new_array_copy>rule_int,
        new_array_copy,
        0,
        )
    case "<":
        rule_array = np.where(  new_array_copy<rule_int,
        new_array_copy,
        0,
        )
    case "=":
        rule_array = np.where(  
        new_array_copy == rule_int,
        new_array_copy,
        0,
        )

print("rule array: \n ",rule_array)
print("r_a mean(0): \n",rule_array.mean(2))
print("mean(1): \n",rule_array.mean(1))