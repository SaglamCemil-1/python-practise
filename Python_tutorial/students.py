"""
names = []
live = []
with open("students.csv") as file:
    for line in file:
        new_list = line.rstrip().split(",")
        names.append(new_list[0])
        live.append(new_list[1])


i = 0
for name in names:
    print(name,end = "")
    print(" lives in : ",live[i])   
    i +=1
"""
"""
namesandplaces = dict(zip(names,live))

for k in namesandplaces:
    if k == "Cem":
        print("this place is not available")
    else:
        print(f"{k} lives in {namesandplaces[k]}")

#veya önemli ve iyi olan yol yapılır 

with open("students.csv") as file:
    for line in file:
        names,lives = line.rstrip().split(",")
        print(f"{name} lives in {lives}")
"""

students = []
with open("students.csv") as file:
    for line in file:
        name,place = line.rstrip().split(",")
        student = {"name":name,"place":place}
        students.append(student)

def getstudentname(student):
    return student["name"]

def getstudentplace(student):
    return student["place"]

#lambda sız : key=getstudentname
for student in sorted(students,key=lambda student: student["name"],reverse=True):
    print(f"{student["name"]} is living in {student["place"]}")

#import csv - reader - dictreader - writer - csvwriter