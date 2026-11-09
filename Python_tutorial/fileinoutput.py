name = input(" what is your name : ")

#open -> doctan bak

                        #fopen - fclose
file = open("fileinpuoutput.txt","a") #append -> ekle
"""
file.write(name)
file.write("\n")
"""
file.write(f"{name}\n")
file.close()


                        #with 
with open("fileinpuoutput.txt","a") as file:
    file.write(f"{name}--2\n")
    

                        #reading -> default
"""
with open("fileinpuoutpu.txt","r") as file:
    lines = file.readlines()
    
    
for line in file:
    print("hello mr/mrs , ", line.rstrip())
"""
                        #sorted version

people = []                        
with open("fileinpuoutpu.txt") as file:
    for line in file:
        people.append(line.rstrip())

for _ in sorted(people,reverse=True):
    print(f"hello ,{_} ")

#yada for line in sorted(file) - print(f"hello ,{line.rstrip()} ") gelebilirdi

                        #CSV comma sperated values

